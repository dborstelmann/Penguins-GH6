def add_unique_demographics_to_profile(profile):
    if "woman" in profile and "family" in profile:
        profile.add("woman_with_child")

    return profile

def recomendations(id): #accept applications
    from dateutil.relativedelta import relativedelta
    from api.models import Client, EmploymentEducation, HealthAndDV, ContinuumServices
    import datetime

    c = Client.objects.filter(uuid=id).first()
    if c is None:
        return {"status": "error", "message": "Client does not exist"}

    e = EmploymentEducation.objects.filter(personal_id=id).first()
    if e is None:
        return {"status": "error", "message": "Employment Education does not exist"}

    h = HealthAndDV.objects.filter(personal_id=id).first()
    if h is None:
        return {"status": "error", "message": "Health and DV does not exist"}

    age = relativedelta(datetime.date.today(), c.date_of_birth).years

    profile = set({})

    if age < 18:
        profile.add("youth")

    if age > 65:
        profile.add("long_term_care")

    if c.veteran == 1:
        profile.add("veteran")

    if c.gender == 0:
        profile.add("woman")
    elif c.gender == 1:
        profile.add("man")
    elif c.gender in (2, 3):
        pfofile.add("transgender")

    if e.last_grade_completed < 4:
        profile.add("eduction")

    if e.employed == 0:
        profile.add("unemployed")
    elif "unemployed" not in profile and e.employment_type > 1:
        profile.add("underemployed")
    else:
        profile.add('benefits')

    if h.domestic_violence_victim == 1:
        profile.add("domestic_violence")

    if h.general_health_status == 5:
        profile.add("general_health")

    if h.mental_health_status in (4, 5):
        profile.add("mental_health")

    if h.pregnancy_status == 1:
        profile.add("pregnant")

    if "pregnant" in profile and relativedelta(datetime.date.today(), h.due_date).days < 30:
        profile.add("general_health")


    reccomendations = ContinuumServices.objects.getMembersFromProfile(profile)

    return reccomendations

def urgency(id):
    from dateutil.relativedelta import relativedelta
    from api.models import Client, EmploymentEducation, HealthAndDV
    import datetime

    c = Client.objects.filter(uuid=id).first()
    if c is None:
        return {"status": "error", "message": "Client does not exist"}

    e = EmploymentEducation.objects.filter(personal_id=id).first()
    if e is None:
        return {"status": "error", "message": "Employment Education does not exist"}

    h = HealthAndDV.objects.filter(personal_id=id).first()
    if h is None:
        return {"status": "error", "message": "Health and DV does not exist"}

    age = relativedelta(datetime.date.today(), c.date_of_birth).years

    return 0
