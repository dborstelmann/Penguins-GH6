from django.db import models

class HealthAndDVManager(models.Manager):
    pass

class HealthAndDV(models.Model):
    objects = HealthAndDVManager()
    personal_id = models.CharField(max_length=15)
    project_entry_id = models.CharField(null=True, max_length=15)
    health_and_dv_id = models.CharField(null=True, max_length=15)
    information_date = models.DateField(null=True)
    domestic_violence_victim = models.IntegerField(null=True)
    when_occured = models.IntegerField(null=True)
    currently_fleeing = models.IntegerField(null=True)
    general_health_status = models.IntegerField(null=True)
    dental_health_status = models.IntegerField(null=True)
    mental_health_status = models.IntegerField(null=True)
    pregnancy_status = models.IntegerField(null=True)
    due_date = models.DateField(null=True)
    data_collection_stage = models.IntegerField(null=True)
    date_created = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)
    associate_id = models.CharField(max_length=15)
