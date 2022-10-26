from django.db import models
from django.urls import reverse

# Create your models here.

TIME = (
    ('D','Dawn'),
    ('N','Noon'),
    ('A','Afternoon'),
    ('E','Evening'),
    ('L','Latenight')
)
class Celeb(models.Model):
    name= models.CharField(max_length=50)
    description= models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('celebs_detail', kwargs={'pk': self.id})

class Tea(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    witnesses = models.IntegerField()
    celebs = models.ManyToManyField(Celeb)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tea_id': self.id})

class Sighting(models.Model):
  date = models.DateField('Sighting Date')
  time = models.CharField('Time of day',
    max_length=1,
    choices=TIME,
    default=TIME[0][0]
  )
  tea = models.ForeignKey(Tea, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"

#   class Meta:
#     ordering=['-date']
