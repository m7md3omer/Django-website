from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Exception:
        raise Http404('album does not exist')
    return render(request, 'music/detail.html', {'album': album})
