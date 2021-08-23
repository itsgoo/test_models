from django.contrib.auth.models import AbstractUser
from django.db import models




class Organization(models.Model):
    name = models.CharField(verbose_name='Name', max_length=45)






class CustomUser(AbstractUser):
    org = models.CharField(verbose_name='organization', max_length=45, null=True)

