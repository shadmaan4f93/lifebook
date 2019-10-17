from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
from home import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('home.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'accounts/', include('accounts.urls', namespace = "accounts")),
    url(r'social/', include('social.urls', namespace = "social")),
    path('admin/', admin.site.urls),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)