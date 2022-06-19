from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.title