from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    datetime = models.DateTimeField()

    def __str__(self):
        # return ' , '.join([str(self.datetime), self.title])
        return self.title
