from django import forms
from .models import UserPost, News, Event
from social.widgets import MediumEditorTextarea


class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('user_post_description',)   
        widgets = {
            'user_post_description': MediumEditorTextarea,       
        }


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = ('date', )
        widgets = {
            'news_detail': MediumEditorTextarea,
        }

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'event_class', 'event_detail', 'start_date','end_date',)   
        widgets = {
            'event_detail': forms.Textarea(attrs={      
            'required': True, 
            'placeholder': 'Event detail'
        }),
            'title': forms.TextInput(attrs={      
            'required': True, 
            'placeholder': 'Title'
        }),
            'start_date': forms.TextInput(attrs={      
                'required': True, 
                'placeholder': 'Start date'
        }),
            'end_date': forms.TextInput(attrs={      
                'required': True, 
                'placeholder': 'End date'
        }),
            'event_class': forms.HiddenInput()       
        }   

