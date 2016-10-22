from django.db import models

class IncomeBenefitsManager(models.Manager):
    pass

class IncomeBenefits(models.Model):
    objects = IncomeBenefitsManager()
    personal_id = models.CharField(max_length=15)
    project_entry_id = models.CharField(max_length=15)
    income_benefits_id = models.CharField(max_length=15)
    information_date = models.DateField(null=True)
    income_from_any_source = models.FloatField(null=True)
    total_monthly_income = models.FloatField(null=True)
    earned = models.NullBooleanField()
    earned_amount = models.FloatField(null=True)
    unemployment = models.NullBooleanField()
    unemployment_amount = models.FloatField(null=True)
    ssi = models.NullBooleanField()
    ssi_amount = models.FloatField(null=True)
    ssdi = models.NullBooleanField()
    ssdi_amount = models.FloatField(null=True)
    va_disability_service = models.NullBooleanField()
    va_disability_service_amount = models.FloatField(null=True)
    va_disability_non_service = models.NullBooleanField()
    va_disability_non_service_amount = models.IntegerField(null=True)
    private_disability = models.NullBooleanField()
    private_disability_amount = models.IntegerField(null=True)
    workers_comp = models.NullBooleanField()
    workers_comp_amount = models.FloatField(null=True)
    tanf = models.NullBooleanField()
    tanf_amount = models.FloatField(null=True)
    ga = models.NullBooleanField()
    ga_amount = models.FloatField(null=True)
    soc_sec_retirement = models.NullBooleanField()
    soc_sec_retirement_amount = models.IntegerField(null=True)
    pension = models.NullBooleanField()
    pension_amount = models.FloatField(null=True)
    child_support = models.NullBooleanField()
    child_support_amount = models.FloatField(null=True)
    alimony = models.NullBooleanField()
    alimony_amount = models.FloatField(null=True)
    other_income_source = models.NullBooleanField()
    other_income_source_amount = models.IntegerField(null=True)
    other_income_source_identify = models.CharField(max_length=126, null=True)
    benefits_from_any_source = models.NullBooleanField()
    snap = models.NullBooleanField()
    wic = models.NullBooleanField()
    tanf_child_care = models.NullBooleanField()
    tanf_transportation = models.NullBooleanField()
    other_tanf = models.NullBooleanField()
    rental_assistance_ongoing = models.NullBooleanField()
    rental_assistance_temp = models.NullBooleanField()
    other_benefits_source = models.NullBooleanField()
    other_benefits_source_identify = models.CharField(max_length=126, null=True)
    insurance_from_any_source = models.NullBooleanField()
    medicaid = models.NullBooleanField()
    no_medicaid_reason = models.IntegerField(null=True)
    medicare = models.NullBooleanField()
    no_medicare_reason = models.IntegerField(null=True)
    schip = models.NullBooleanField()
    no_schip_reason = models.CharField(max_length=126, null=True)
    va_medical_services = models.NullBooleanField()
    no_va_med_reason = models.CharField(max_length=126, null=True)
    employer_provided = models.NullBooleanField()
    no_employer_provided_reason = models.CharField(max_length=126, null=True)
    cobra = models.NullBooleanField()
    no_cobra_reason = models.CharField(max_length=126, null=True)
    private_pay = models.NullBooleanField()
    no_private_pay_reason = models.CharField(max_length=126, null=True)
    state_health_ins = models.NullBooleanField()
    no_state_health_ins_reason = models.CharField(max_length=126, null=True)
    hiv_aids_assistance = models.NullBooleanField()
    no_hiv_aids_assistance_reason = models.CharField(max_length=126, null=True)
    adap = models.NullBooleanField()
    no_adap_reason = models.CharField(max_length=126, null=True)
    data_collection_stage = models.IntegerField(null=True)
    date_created = models.DateTimeField(null=False)
    date_updated = models.DateTimeField(null=False)
    associate_id = models.CharField(max_length=15)
