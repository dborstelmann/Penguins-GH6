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

    def recomendations(self, a): #accept applications
        from dateutil.relativedelta import relativedelta
        import datetime
        age = relativedelta(datetime.date.today(), a.birthday).years

        POSSIBLE_AILMENTS = [
            "doctor",
            "sick",
            "medicine",
            "rehab",
            "hospital"
        ]

        POSSIBLE_BENEFITS = [
            "case",
            "child",
            "care",
            "education",
            "school",
            "employment",
            "housing",
            "legal",
            "mentor",
            "support"
        ]

        POSSIBLY_HOMELESS = [
            "homeless",
            "street",
            "evict",
            "out"
        ]

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

        if any(substring in a.why.lower() for substring in POSSIBLY_HOMELESS):
            profile.add("homeless")

        if any(substring in a.why.lower() for substring in POSSIBLE_AILMENTS):
            profile.add("health")

        if any(substring in a.why.lower() for substring in POSSIBLE_BENEFITS):
            profile.add("benefits")

        reccomendations = []

        if "health" in profile and "homeless" in profile:
            reccomendations += self.getMembersFromTag("Health", profile)

        if "domestic_violence" in profile:
            reccomendations += self.getMembersFromTag("DViolence", profile)

        if "single" in profile:
            reccomendations += self.getMembersFromTag("SingleMW", profile)

        if "prevention" in profile:
            reccomendations += self.getMembersFromTag("Prevention", profile)

        if "veteran" in profile:
            reccomendations += self.getMembersFromTag("Veteran", profile)

        if "benefits" in profile:
            reccomendations += self.getMembersFromTag("Benefits", profile)

        if "women" in profile and "family" in profile:
            reccomendations += self.getMembersFromTag("WWChild", profile)

        if "youth" in profile and "homeless" in profile:
            reccomendations += self.getMembersFromTag("HYouth", profile)

        if "homeless" in profile and "family" in profile:
            reccomendations += self.getMembersFromTag("HFamilies", profile)

        return reccomendations

    def getMembersFromTag(self, tag, profile):
        clist = ContinuumMembers.objects.filter(services_offered__contains=tag).exclude(criteria_required__in=profile)
        return [{
            "name": m.name,
            "website": m.website
        } for m in clist]


class ContinuumServices(models.Model):
    objects = ContinuumServicesManager()
    tag = models.CharField(max_length=10) # shortend name
    name = models.CharField(max_length=63)
    description = models.TextField(null=True)


class ContinuumMembers(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    services_offered = models.CharField(max_length=255, null=True)
    criteria_required = models.CharField(max_length=255, null=True)
