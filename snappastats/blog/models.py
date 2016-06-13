from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    date_published = models.DateField('date published')

    def __str__(self):
        return '{} ({})'.format(self.title, self.date_published)
