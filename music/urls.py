from . import views
from django.urls import path


app_name = 'music'
urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # /songs/
    path('songs/', views.SongsView.as_view(), name='songs'),


    # /music/<pk>/
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/3/
    path('album/<int:<pk>>', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/3/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/album/3/add/
    path('album/<int:pk>/song', views.SongCreate.as_view(), name='song-create'),

    path('album/<int:pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),

]
