from django.db import models


class ApplicantManager(models.Manager):

    def calculate_urgency(self, c):
        from dateutil.relativedelta import relativedelta
        import datetime
        age = relativedelta(datetime.date.today(), c.birthday).years

        score = 0
        if c.address is None or c.address.lower() == 'homeless' or c.address.lower() == 'n/a':
            score += 15

        if c.gender == 0: #female
            score += 2

        if c.gender in [ 2, 3, 4 ]:
            score += 3

        if c.veteran == 1:
            score += 3

        if c.family == "family":
            score += 2

        if c.pregnancy:
            score += 4

        if c.drug:
            score += 5

        if age < 25:
            score += 25 - age

        if age > 60:
            score += age - 60

        return int( (float(score) / 40)  * 100 )

class Applicant(models.Model):
    objects = ApplicantManager()
    first_name = models.CharField(max_length=63, null=True)
    last_name = models.CharField(max_length=63, null=True)
    why = models.CharField(max_length=1025, null=True)
    phone = models.CharField(max_length=63, null=True)
    email = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=63, null=True)
    birthday = models.DateField()
    ethnicity = models.IntegerField(null=False, default=99) # Keys for races
    gender = models.IntegerField(null=False, default=99) # Using boolean as a binary 1=F 0=M
    veteran = models.IntegerField(null=False, default=99)
    family = models.CharField(max_length=63, null=True)
    domestic_violence = models.IntegerField(null=True)
    pregnancy = models.BooleanField()
    drug = models.BooleanField()
    urgency = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)
    uuid = models.CharField(max_length=63, null=True)
