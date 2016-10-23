def add_unique_demographics_to_profile(profile):
    if "woman" in profile and "family" in profile:
        profile.add("woman_with_child")

    return profile

def build_profile(id):
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
        profile.add("education")

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

    return profile

def recomendations(id): #accept applications
    from api.models import ContinuumServices
    return ContinuumServices.objects.getMembersFromProfile(build_profile(id))

def urgency(id):
    profile = build_profile(id)
    score = 0

    if "youth" in profile:
        score += 10

    if "long_term_care" in profile:
        score += 10

    if "transgender" in profile:
        score += 5

    if "woman" in profile:
        score += 3

    if "education" in profile:
        score += 5

    if "unemployed" in profile:
        score += 10

    if "underemployed" in profile:
        score += 5

    if "domestic_violence" in profile:
        score += 15

    if "general_health" in profile or "mental_health" in profile:
        score += 5

    if "pregnant" in profile:
        score += 10
        
    return int( ( float(score) / 50 ) * 100 )
