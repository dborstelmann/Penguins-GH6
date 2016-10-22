from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

class SheltersManager(models.Manager):

    def add_client(c):
        c.occupancy = c.occupancy + 1
        assert c.occupancy <= c.max_occupancy
        c.last_updated = datetime.datetime.now()
        c.save()

    def remove_client(c):
        c.occupancy = c.occupancy - 1
        assert c.occupancy >= 0
        c.last_updated = datetime.datetime.now()
        c.save()

    def get_availability(c):
        return c.max_occupancy - c.occupancy

class Shelters(models.Model):
    objects = SheltersManager()
    name = models.CharField(max_length=63)
    address = models.CharField(max_length=63)
    max_occupancy = models.IntegerField()
    occupancy = models.IntegerField()
    last_updated = models.DateTimeField(null=True)

class ContinuumServicesManager(models.Manager):

    def recomendations(a): #accept applications
        pass

class ContinuumServices(models.Model):
    tag = models.CharField(max_length=10) # shortend name
    name = models.CharField(max_length=63)
    description = models.TextField(null=True)


class ContinuumMembers(models.Model):
    name = models.CharField(max_length=31)
    website = models.CharField(max_length=63)
    services_offered = ArrayField(models.CharField(max_length=31), size=6) #array of ContinumService ID's
