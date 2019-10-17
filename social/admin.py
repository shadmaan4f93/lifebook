from django import forms
from django.contrib import admin
from django.db import models
from .models import UserPost, News, Event

from .widgets import MediumEditorTextarea

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = ('date', )
        widgets = {
            'news_detail': MediumEditorTextarea,
        }

class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    formfield_overrides = {
        models.TextField: {"widget": MediumEditorTextarea}
    }


# Register your models here.
admin.site.register(UserPost)
admin.site.register(Event)
admin.site.register(News, NewsAdmin)


