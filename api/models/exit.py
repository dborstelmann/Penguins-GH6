from django.db import models

class ExitManager(models.Manager):
    pass

class Exit(models.Model):
    objects = ExitManager()
    personal_id = models.CharField(max_length=15)
    project_entry_id = models.CharField(max_length=15)
    exit_id = models.CharField(max_length=15)
    exit_date = models.DateField()
    destination = models.IntegerField(null=True)
    other_destination = models.IntegerField(null=True)
    assessment_disposition = models.IntegerField(null=True)
    other_disposition = models.IntegerField(null=True)
    housing_assessment = models.IntegerField(null=True)
    subsidy_information = models.IntegerField(null=True)
    connection_with_soar = models.IntegerField(null=True)
    written_after_care_plan = models.IntegerField(null=True)
    assistance_mainstream_benefits = models.IntegerField(null=True)
    permanent_housing_placement = models.IntegerField(null=True)
    temporary_shelter_placement = models.IntegerField(null=True)
    exit_counseling = models.IntegerField(null=True)
    further_follow_up_services = models.IntegerField(null=True)
    scheduled_follow_up_contact = models.IntegerField(null=True)
    resource_package = models.IntegerField(null=True)
    other_aftercare_plan_or_action = models.IntegerField(null=True)
    project_completion_status = models.IntegerField(null=True)
    early_exit_reason = models.IntegerField(null=True)
    family_reunification_achieved = models.IntegerField(null=True)
    date_created = models.DateTimeField(null=False)
    date_updated = models.DateTimeField(null=False)
    associate_id = models.CharField(max_length=15)
