from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^(?P<page>[A-Za-z0-9.-]+)/page$', views.pages, name='pages'),
               url(r'^profile/(?P<shortname>[A-Za-z0-9.-]+)$', views.profiles, name='profiles'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
