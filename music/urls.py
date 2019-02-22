from . import views
from django.conf.urls import url

app_name = 'music'
urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]