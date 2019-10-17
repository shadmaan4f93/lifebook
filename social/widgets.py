from __future__ import unicode_literals
import json
from django import forms
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from django.utils.html import escape

from skflite import settings



class MediumEditorTextarea(forms.Textarea):

    def render(self, name, value, attrs=None, renderer=None):

        if attrs is None:
            attrs = {}
        attrs.update({'class': 'django-mediumeditor-input'})

        identifier = attrs.get('id', 'id_{}'.format(name))
        params = {
            'data-mediumeditor-textarea': identifier,
            'class': 'django-mediumeditor-editable',
            'id': '{}_editable'.format(identifier),
        }
        param_str = ' '.join('{}="{}"'.format(k, v) for k, v in params.items())
        html = super(MediumEditorTextarea, self).render(name, value, attrs)
        options = json.dumps(settings.MEDIUM_EDITOR_OPTIONS)
        html = mark_safe(u'''{}
            <div {}></div>
            <script type="text/javascript">
                MediumEditorOptions={};
            </script>'''.format(html, param_str, options))
        return html

    class Media:
        css = {'all': (
            '//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css',
            '//cdn.jsdelivr.net/medium-editor/latest/css/medium-editor.min.css',
            'css/mediumeditor/django-mediumeditor.css',
            '//cdn.jsdelivr.net/medium-editor/latest/css/themes/{}.min.css'.format(
                settings.MEDIUM_EDITOR_THEME
            ),
            '//cdnjs.cloudflare.com/ajax/libs/medium-editor-insert-plugin/2.4.1/css/medium-editor-insert-plugin.min.css'
        )}
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/jquery-sortable/0.9.13/jquery-sortable-min.js',
            '//cdn.jsdelivr.net/medium-editor/latest/js/medium-editor.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/handlebars.js/4.0.11/handlebars.runtime.min.js',
            #jQuery-File-Upload dependencies 
            'mediumeditor/js/mediumeditor/jquery-ui.min.js',
            'mediumeditor/js/mediumeditor/jquery.iframe-transport.min.js',
            'mediumeditor/js/mediumeditor/jquery.fileupload.min.js',
            'mediumeditor/js/mediumeditor/medium-editor-insert-plugin.min.js',
            'js/custom-mediumeditor.js', 
        )
