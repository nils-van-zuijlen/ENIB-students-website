from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
import django.forms as forms
import django.forms.widgets as widgets
from .models import Poll
from collections import OrderedDict
import json


class QuestionWidget(forms.widgets.TextInput):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.qid = parent.qid
        self.answers = parent.answers
        self.data = parent.data

    def render(self, name="", value="", **kwargs):
        return render_to_string("poll/question_widget.html",
            {'qid': self.qid[1:],
             'real_qid': self.qid,
             'question_form': super().render(name=name, value=value, **kwargs),
             'answers': [forms.widgets.TextInput().render(name=answer, value=self.data[answer], attrs={'id': answer}) for answer in self.answers],
            }
        )


class QuestionField(forms.Field):
    def __init__(self, qid, answers, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.qid = str(qid)
        self.answers = answers
        self.data = data
        self.widget = QuestionWidget(self)


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ['title', 'group', 'contributor_only']
        widgets = {'title': widgets.TextInput,
                   'start_time': forms.SplitDateTimeWidget,
                   'end_time': forms.SplitDateTimeWidget,
                    }
    start_time = forms.SplitDateTimeField()
    end_time = forms.SplitDateTimeField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        try:
            initial_q_a = kwargs.pop('initial_q_a')
        except KeyError:
            initial_q_a = None
        super().__init__(*args, **kwargs)

        self.q_a_nb = "{}"
        self.questions_answers = OrderedDict()
        for f in ['start_time', 'end_time']:
            self.fields[f].widget.attrs['id'] = f

        if not len(args) and not initial_q_a:  # If the request is empty
            return

        self.questions = []
        self.answers = []
        if initial_q_a is not None:
            self._init(initial_q_a)

        # Build a list of questions and answers out of the request
        if initial_q_a is None:
            for arg in args[0]:
                if arg.startswith('q'):
                    self.questions.append(arg)
                if arg.startswith('a'):
                    self.answers.append(arg)

        nb_q = 1
        # Association of questions and answers
        for q in sorted(self.questions, key=lambda x: int(x[1:])):
            nb_a = 1
            self.questions_answers[q] = []
            for a in sorted(self.answers, key=lambda x: int(x[1:].split("_")[0])):
                if not a.endswith(q):
                    continue
                self.questions_answers[q].append(a)
                nb_a += 1
            self.fields[q] = QuestionField(qid=q, answers=self.questions_answers[q], data=self.data, initial=self.data[q], label="Question " + str(nb_q))
            nb_q += 1
        self.q_a_nb = json.dumps({q[1:]: len(a) for q, a in self.questions_answers.items()})

    def _init(self, q_a):
        for i, (q, answers) in enumerate(q_a.items()):
            qid = "q" + str(i)
            self.data[qid] = q.text
            self.questions.append(qid)
            for j, a in enumerate(answers):
                aid = "a" + str(j) + "_q" + str(i)
                self.data[aid] = a.text
                self.answers.append(aid)

    def js(self):
        return mark_safe('''<script>
            create_calendar("start_time_0");
            create_calendar("end_time_0");
        </script>
        ''')

    def clean(self):
        cleaned_data = super().clean()
        err_no_answer = False
        err_empty_answer = False
        err_empty_question = False
        if not self.questions_answers:
            self.add_error(None, "Il doit y avoir au moins une question")
        for q, a in self.questions_answers.items():
            if len(a) < 2 and not err_no_answer:
                err_no_answer = True
                self.add_error(None, "Chaque question doit avoir au minimum 2 réponses possibles.")
            if not self.data[q] and not err_empty_question:
                err_empty_question = True
                self.add_error(None, "Vous ne pouvez pas avoir de question vide")
            for answer in a:
                cleaned_data[answer] = forms.CharField(required=False).clean(self.data[answer])
                if not cleaned_data[answer] and not err_empty_answer:
                    err_empty_answer = True
                    self.add_error(None, "Vous ne pouvez pas avoir de réponse vide")
        if cleaned_data.get('start_time') and cleaned_data.get('end_time'):
            if cleaned_data['start_time'] >= cleaned_data['end_time']:
                self.add_error('start_time', "Le début du sondage doit etre avant la fin")
        return cleaned_data


