from django.db import models
from django.urls import reverse

# Create your models here.
class Tea(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    witnesses = models.IntegerField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tea_id': self.id})
