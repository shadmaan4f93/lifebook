from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from django.utils.html import escape
from django import forms

class CustomSelectWidget(forms.TextInput):
        
    def render(self, name, value, attrs= None):
        name = name
        value = value
        html = [u'<div class="custom-tile"><ul>']
        if hasattr(self, 'choices'):
            for k, v in self.choices:
                if (k == value):
                    html.append(u"<li data='%s' class='active'>%s</li>" % (escape(k), escape(v)))     
                else:
                    html.append(u"<li data='%s'>%s</li>" % (escape(k), escape(v))) 
        else:
            html.append(u"<li>This widgits will not apply for this field</li>")                    
        html.append(u'</ul></div>')
        html.append(u'<input %s name="%s" hidden type="text" value="%s">'% (flatatt(attrs), escape(name), escape(value)))
        
        return mark_safe(u'\n'.join(html))

    class Media:
        css = {
        'all': ('./css/customselectwidget.css',)
        }
        js = ('./js/customselectwidget.js',)
