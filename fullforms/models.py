from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FullForms(models.Model):
    shortForm = models.CharField(max_length=255)
    fullForm = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, null=True)
    approve = models.BooleanField(default=False)
    
    def __str__(self):
        return self.shortForm + ' - ' + self.fullForm


user_points = models.IntegerField(default=0)
user_points.contribute_to_class(User, 'points')
