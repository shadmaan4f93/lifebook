from django.conf.urls import url
from django.contrib.auth.views import (
LoginView,
LogoutView,
PasswordResetView,
PasswordResetConfirmView,
PasswordResetDoneView,
PasswordResetCompleteView,
PasswordChangeView,
PasswordChangeDoneView,
)

from .views import edit_profile
from . import views

app_name = "accounts"
urlpatterns = [
    url(r'settings/accounts/$', views.accounts_settings, name='accounts_settings'),
    url(r'settings/general/$', views.general_settings, name='general_settings'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', LoginView.as_view(), {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': '/accounts/login'}, name='logout'),
    url(r'^user/profile/$', views.profile, name='Profile'),
    url(r'^user/profile/friend/(?P<pk>.+)/$', views.friend_profile, name='Friend_Profile'),
    url(r'^user/profile/add/$', views.add_user_info, name='add_user_info'),
    url(r'^user/profile/update/$', views.update_user_info, name='update_user_info'),
    url(r'^profile/edit/$', views.edit_profile, name='Profile-update'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^activate/(?P<uidb64>.+)/(?P<token>.+)/$', views.activate, name='activate'),
    url(r'connect/(?P<operation>.+)/(?P<pk>.+)/$', views.change_friend, name='change_friend'),
]
