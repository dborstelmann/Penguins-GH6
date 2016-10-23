from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from django.db.models import Q
from api.helpers import add_unique_demographics_to_profile
from utils import value_maps

class SheltersManager(models.Manager):

    pass

class Shelters(models.Model):
    objects = SheltersManager()
    name = models.CharField(max_length=63)
    address = models.CharField(max_length=63)
    max_occupancy = models.IntegerField()
    occupancy = models.IntegerField()
    requirements = models.CharField(max_length=63, null=True)
    last_updated = models.DateTimeField(null=True)

class ContinuumServicesManager(models.Manager):

    def recomendations(self, a): #accept applications
        from dateutil.relativedelta import relativedelta
        import datetime
        age = relativedelta(datetime.date.today(), a.birthday).years

        profile = set({})
        if ( a.address is None ) or ( not a.address ):
            profile.add("homeless")

        if a.address:
            profile.add("prevention")

        if age < 18:
            profile.add("youth")

        if a.gender in (0, 2):
            profile.add("woman")

        if a.veteran:
            profile.add("veteran")

        if a.family == 'family':
            profile.add("family")

        if a.family == 'individual':
            profile.add("single")

        if a.domestic_violence:
            profile.add("domestic_violence")

        if a.drug:
            profile.add("health")

        if any(substring in a.why.lower() for substring in value_maps.POSSIBLY_HOMELESS):
            profile.add("homeless")

        if any(substring in a.why.lower() for substring in value_maps.POSSIBLE_AILMENTS):
            profile.add("health")

        if any(substring in a.why.lower() for substring in value_maps.POSSIBLE_BENEFITS):
            profile.add("benefits")

        if any(substring in a.why.lower() for substring in ("HIV", "AIDS")):
            profile.add("AIDS")

        reccomendations = self.getMembersFromProfile(profile)

        return reccomendations

    def getMembersFromProfile(self, profile):
        profile = add_unique_demographics_to_profile(profile)
        clist = ContinuumMembers.objects.filter(services_offered__in=profile)
        return [{
            "name": m.name,
            "website": m.website
        } for m in clist if (m.criteria_required in profile or not m.criteria_required)]


class ContinuumServices(models.Model):
    objects = ContinuumServicesManager()
    tag = models.CharField(max_length=10) # shortend name
    name = models.CharField(max_length=63)
    description = models.TextField(null=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class ContinuumMembers(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    services_offered = models.CharField(max_length=255, null=True)
    criteria_required = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)
