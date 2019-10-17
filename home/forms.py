from django import forms
from .models import Question
from .widgets import CustomSelectWidget

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    comments = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': 4, 'cols': 40, 'placeholder': 'Comments'}))


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('Subject_name', 'question', 'image' )
        labels = {
            'Subject_name': 'Select subject',
            'question': 'Enter question',
            'image': 'Attech file'         
        }
        help_texts = {
            'Subject_name': 'Please select subject that we can explain better',
            'question': 'Mention question detail',
            'image': 'Attech image, doc if anny'
        }
        widgets = {
            'Subject_name': CustomSelectWidget,       
        }

class ReviewForm(forms.Form):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    comments = forms.CharField(widget=forms.Textarea, required=True)


class ScrapyForm(forms.Form):
    url = forms.URLField(required=True)
    element = forms.CharField(required=True)
