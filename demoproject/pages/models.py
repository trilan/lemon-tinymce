from django.db import models


class Page(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField()
