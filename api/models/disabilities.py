from django.db import models

class DisabilityManager(models.Manager):
    pass

class Disabilities(models.Model):
    objects = DisabilityManager()
    personal_id = models.CharField(max_length=15)
    project_entry_id = models.CharField(max_length=15)
    disabilities_id = models.CharField(max_length=15)
    information_date = models.DateField(null=False)
    disability_type = models.IntegerField(null=False) #Keys for a disability
    disability_response = models.IntegerField(null=False)
    indefinite_and_impairs = models.IntegerField(null=True)
    documentation_on_file = models.IntegerField(null=True)
    receiving_services = models.IntegerField(null=True)
    path_how_confirmed = models.IntegerField(null=True)
    data_collection_stage = models.IntegerField(null=True)
    date_created = models.DateField(null=False)
    date_updated = models.DateField(null=False)
    associate_id = models.CharField(max_length=15)
