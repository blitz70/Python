from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return ":".join([str(self.date), str(self.title), str(self.artist)])


class Song(models.Model):
    # part of Album, will be erased when associated Album is deleted
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return " , ".join([str(self.date), str(self.title)])
