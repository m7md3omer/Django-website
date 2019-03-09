from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='media')

    def __str__(self):
        return str(self.artist) + "  " + str(self.album_name)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    file = models.FileField(default='default.mp3', upload_to='songs')

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('music:index')
