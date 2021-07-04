from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published_at = models.DateField(default='', blank=False)
    done = models.BooleanField(default=False, blank=False)
