from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Post(models.Model):
    image = ImageField()
    description = models.CharField(max_length=140, blank=True, null=True)
    

    def __str__(self):
        return self.description
    