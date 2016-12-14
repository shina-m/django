from django.db import models
from django.core.validators import validate_email

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=False, validators=[validate_email, ])
   # pub_date = models.DateTimeField('date published')

    class Admin:
        pass

def __unicode__(self):
    return self.first_name