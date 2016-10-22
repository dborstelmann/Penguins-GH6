from django.db import models

class ClientManager(models.Manager):
  pass

class Client(models.Model):
      objects = ClientManager()
      uuid = models.CharField(max_length=15) # id to match client with meta info
      first_name = models.CharField(max_length=63, null=False, blank=True)
      middle_name = models.CharField(max_length=63, null=False, blank=True)
      last_name = models.CharField(max_length=63, null=False, blank=True)
      social_security = models.CharField(max_length=63, null=False, blank=True)
      date_of_birth = models.DateField()
      ethnicity = models.IntegerField(null=False) # Keys for races
      gender = models.BooleanField(null=False) # Using boolean as a binary 1=F 0=M
      veteran = models.BooleanField(null=False)
      year_entered = models.IntegerField()
      year_exited = models.IntegerField()
      war_participated = models.IntegerField() # Keys for wars
      military_branch = models.IntegerField() # Keys for branches
      discharge_status = models.IntegerField() # Keys for status
      created = models.DateField()
      updated = models.DateField()
      associate_id = models.CharField(max_length=15)
