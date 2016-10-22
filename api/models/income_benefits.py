from django.db import models

class IncomeBenefitsManager(models.Manager):
    pass

class IncomeBenefits(models.Model):
    objects = IncomeBenefitsManager()
    personal_id = models.CharField(max_length=15)
    project_entry_id = models.CharField(max_length=15)
    income_benefits_id = models.CharField(max_length=15)
    information_date = models.DateField(null=True)
    income_from_any_source = models.IntegerField(null=True)
    total_monthly_income = models.IntegerField(null=True)
    earned = models.BooleanField()
    earned_amount = models.IntegerField(null=True)
    unemployment = models.BooleanField()
    unemployment_amount = models.IntegerField(null=True)
    ssi = models.BooleanField()
    ssi_amount = models.IntegerField(null=True)
    ssdi = models.BooleanField()
    ssdi_amount = models.IntegerField(null=True)
    va_disability_service = models.BooleanField()
    va_disability_service_amount = models.IntegerField(null=True)
    va_disability_non_service = models.BooleanField()
    va_disability_non_service_amount = models.IntegerField(null=True)
    private_disability = models.BooleanField()
    private_disability_amount = models.IntegerField(null=True)
    workers_comp = models.BooleanField()
    workers_comp_amount = models.IntegerField(null=True)
    tanf = models.BooleanField()
    tanf_amount = models.IntegerField(null=True)
    ga = models.BooleanField()
    ga_amount = models.IntegerField(null=True)
    soc_sec_retirement = models.BooleanField()
    soc_sec_retirement_amount = models.IntegerField(null=True)
    pension = models.BooleanField()
    pension_amount = models.IntegerField(null=True)
    child_support = models.BooleanField()
    child_support_amount = models.IntegerField(null=True)
    alimony = models.BooleanField()
    alimony_amount = models.IntegerField(null=True)
    other_income_source = models.BooleanField()
    other_incount_source_amount = models.IntegerField(null=True)
    other_income_source_identify = models.CharField(max_length=126, null=True)
    benefits_from_any_source = models.BooleanField()
    snap = models.BooleanField()
    wic = models.BooleanField()
    tanf_child_care = models.BooleanField()
    tanf_transportation = models.BooleanField()
    other_tanf = models.BooleanField()
    rental_assistance_ongoing = models.BooleanField()
    rental_assistance_temp = models.BooleanField()
    other_benefits_source = models.BooleanField()
    other_benefits_source_identify = models.CharField(max_length=126, null=True)
    insurance_from_any_source = models.NullBooleanField()
    medicaid = models.BooleanField()
    no_medicaid_reason = models.IntegerField(null=True)
    medicare = models.BooleanField()
    no_medicare_reason = models.IntegerField(null=True)
    schip = models.BooleanField()
    no_schip_reason = models.CharField(max_length=126, null=True)
    va_medical_services = models.BooleanField()
    no_va_med_reason = models.CharField(max_length=126, null=True)
    employer_provided = models.BooleanField()
    no_employer_provided_reason = models.CharField(max_length=126, null=True)
    cobra = models.BooleanField()
    no_cobra_reason = models.CharField(max_length=126, null=True)
    private_pay = models.BooleanField()
    no_private_pay_reason = models.CharField(max_length=126, null=True)
    state_health_ins = models.BooleanField()
    no_state_health_ins_reason = models.CharField(max_length=126, null=True)
    hiv_aids_assistance = models.BooleanField()
    no_hiv_aids_assistance_reason = models.CharField(max_length=126, null=True)
    adap = models.BooleanField()
    no_adap_reason = models.CharField(max_length=126, null=True)
    data_collection_stage = models.IntegerField(null=True)
    date_created = models.DateField(null=False)
    date_updated = models.DateField(null=False)
    associate_id = models.CharField(max_length=15)
