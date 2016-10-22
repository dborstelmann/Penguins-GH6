import datetime
from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField

class ClientManager(models.Manager):
  pass

class Client(models.Model):
      objects = ClientManager()
      uuid = models.CharField(max_length=15) # id to match client with meta info
      first_name = models.CharField(max_length=63, null=True, blank=True)
      middle_name = models.CharField(max_length=63, null=True, blank=True)
      last_name = models.CharField(max_length=63, null=True, blank=True)
      social_security = models.CharField(max_length=63, null=True, blank=True)
      date_of_birth = models.DateField(null=True)
      ethnicity = models.IntegerField(null=False, default=99) # Keys for races
      gender = models.IntegerField(null=False, default=99) # Using boolean as a binary 1=F 0=M
      veteran = models.IntegerField(null=False, default=99)
      year_entered = models.IntegerField(null=True)
      year_exited = models.IntegerField(null=True)
      war_participated = ArrayField(models.IntegerField(), default=[]) # Keys for wars
      military_branch = models.IntegerField(null=True) # Keys for branches
      discharge_status = models.IntegerField(null=True) # Keys for status
      date_created = models.DateTimeField(null=False, default=timezone.now)
      date_updated = models.DateTimeField(null=False, default=timezone.now)
      associate_id = models.CharField(max_length=15)
