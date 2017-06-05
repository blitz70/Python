from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.FileField()
    date = models.DateField(auto_now_add=True)  # default today

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return " , ".join([str(self.date), str(self.title), str(self.artist)])


class Song(models.Model):
    # part of Album, will be erased when associated Album is deleted
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    date = models.DateField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return " , ".join([str(self.date), str(self.title)])
