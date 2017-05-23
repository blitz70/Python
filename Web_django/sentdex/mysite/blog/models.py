from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    datetime = models.DateTimeField()

    def __repr__(self):
        return ','.join([self.title, self.body, self.datetime])

    '''def __str__(self):
        return self.title'''