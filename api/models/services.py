from django.db import models

class ServicesManager(models.Manager):
    pass

class Services(models.Model):
    objects = ServicesManager()
    personal_id = models.CharField(max_length=15)
    project_entry_id = models.CharField(max_length=15)
    services_id = models.CharField(max_length=15)
    date_provided = models.DateField()
    record_type = models.IntegerField(null=True)
    type_provided = models.IntegerField(null=True)
    other_type_provided = models.IntegerField(null=True)
    sub_type_provided = models.FloatField(null=True)
    fa_amount = models.FloatField(null=True)
    referral_outcome = models.CharField(max_length=126)
    date_created = models.DateTimeField(null=False)
    date_updated = models.DateTimeField(null=False)
    associate_id = models.CharField(max_length=15)
