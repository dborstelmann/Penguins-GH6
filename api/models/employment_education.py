from django.db import models


class EmploymentEducationManager(models.Manager):
    pass

class EmploymentEducation(models.Model):
    objects = EmploymentEducationManager()
    personal_id = models.CharField(max_length=15)
    project_entry_id = models.CharField(max_length=15)
    employment_education_id = models.CharField(max_length=15)
    information_date = models.DateField(null=True)
    last_grade_completed = models.IntegerField(null=True)
    school_status = models.IntegerField(null=True)
    employed = models.IntegerField(null=True)
    employment_type = models.IntegerField(null=True)
    not_employed_reason = models.IntegerField(null=True)
    data_collection_stage = models.IntegerField(null=True)
    date_created = models.DateTimeField(null=False)
    date_updated = models.DateTimeField(null=False)
    associate_id = models.CharField(max_length=15)
