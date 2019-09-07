from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Contact (models.Model):
    Name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=20)
    information = models.CharField(max_length=50,)
    gender = models.CharField(max_length=20,choices=(
    ('male','Male'),
    ('female','Female')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['-id']
    