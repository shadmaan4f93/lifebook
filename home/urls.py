from django.conf.urls import url
from .api import views as api_views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',  views.index, name='home'),
    url(r'^test/$',  views.test, name='home'),
    url(r'^feedback/$',  views.feedback, name='feedback'),
    url(r'^question/$',  views.question_upload, name='question_upload'),
    url(r'^about/$',  views.about, name='about'),
    url(r'^Members/$',  views.members, name='members'),
    url(
        regex=r'^api/get-username/$',
        view=api_views.get_username,
    ),
    url(
        regex=r'^api/userlist/$',
        view=api_views.get_user_list,
    ),
    url(
        regex=r'^api/userprofile/$',
        view=api_views.get_user_profile,
    ),
    url(
        regex=r'^api/event-list/$',
        view=api_views.get_events,
    ),
    url(
        regex=r'^api/current-user-detail/$',
        view=api_views.current_user_detail,
    ),
    url(
        regex=r'^api/userprofile/(?P<pk>\d+)/$',
        view=api_views.get_user_profile,
    ),
]
   