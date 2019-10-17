from django.conf.urls import url
from . import views
app_name = "social" 
urlpatterns = [
    url(r'^Post/$',  views.user_post, name='post'),
    url(r'^Post/delete/(?P<pk>[0-9]+)$',  views.delete_post, name='delete_post'),
    url(r'^Event/$',  views.events, name='events'),
    url(r'^Event/delete/(?P<pk>[0-9]+)$',  views.delete_events, name='delete_events'),
    url(r'^News/$',  views.news, name='news'),
   
]
    