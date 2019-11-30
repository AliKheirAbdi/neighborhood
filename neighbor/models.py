from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch  import receiver
from django.http import Http404

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    occupants = models.IntegerField()
    image = models.ImageField(default='hood.jpg', upload_to='hood/')
    datecreated = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hood')
    health_department_contact = models.IntegerField()
    police_authority_contact = models.IntegerField()

    def __str__(self):
        return f'{self.name} Neighborhood'

    class Meta:
        db_table ='Neighborhood'

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
