import datetime
from django.http import JsonResponse
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from api.models import ( Applicant, Client, Disabilities, EmploymentEducation,
    Enrollment, HealthAndDV, IncomeBenefits, Services, ContinuumServices, Shelters )

from utils import value_maps
from api import helpers


def search_clients(request):

    '''
        request.POST =
            query
    '''
    clients = Client.objects.all()
    if 'query' in request.POST:
        q = request.POST['query']
        if q.isdigit():
            clients = clients.filter(uuid=q)
        else:
            clients = clients.filter(last_name__icontains=q)


    return JsonResponse([{
        "first_name": c.first_name,
        "middle_name": c.middle_name,
        "last_name": c.last_name,
        "social_security": c.social_security,
        "date_of_birth": datetime.datetime.strftime(c.date_of_birth, '%m/%d/%Y'),
        "ethnicity":  value_maps.race[c.ethnicity],
        "gender": value_maps.gender[c.gender],
        "veteran": value_maps.general_boolean_numbers[c.veteran],
        "year_entered": c.year_entered,
        "year_exited": c.year_exited,
        "date_created": c.date_created,
        "id": c.uuid
    } for c in clients], safe=False)

def get_applicants(request):
    app_list = Applicant.objects.filter(reviewed=False)

    applicant = [{
        "id": c.id,
        "first_name": c.first_name,
        "last_name": c.last_name,
        "why": c.why,
        "phone": c.phone,
        "email": c.email,
        "address": c.address,
        "birthday": c.birthday,
        "ethnicity": value_maps.race[c.ethnicity],
        "gender": value_maps.gender[c.gender],
        "veteran": value_maps.general_boolean_numbers[c.veteran],
        "family": c.family,
        "domestic_violence": value_maps.general_boolean_numbers[c.domestic_violence],
        "pregnancy": c.pregnancy,
        "drug": c.drug,
        "urgency": Applicant.objects.calculate_urgency(c),
        "created": c.created,
        "reviewed": c.reviewed,
        "recommendations": ContinuumServices.objects.recomendations(c)
        } for c in app_list]

    return JsonResponse(applicant, safe=False)

def get_shelters(request):
    shelter_list = Shelters.objects.all()

    shelters = [{
        "id": c.id,
        "name": c.name,
        "address": c.address,
        "max_occupancy": c.max_occupancy,
        "occupancy": c.occupancy,
        "requirements": c.requirements,
        "last_updated": c.last_updated
        } for c in shelter_list]

    return JsonResponse(shelters, safe=False)


def profile(request):
    client_uuid = request.POST['id']
    tab = request.POST['tab']
    cl = Client.objects.filter(uuid=client_uuid).first()
    e = EmploymentEducation.objects.filter(personal_id=client_uuid).first()
    health = HealthAndDV.objects.filter(personal_id=client_uuid).first()
    services = Services.objects.filter(personal_id=client_uuid).first()

    if cl is None or e is None or health is None:
        Client.objects.filter(uuid=client_uuid).delete()
        return JsonResponse({"status": "error", "message": "member not found"})

    profile = {}
    profile = {
        "id": client_uuid,
        "associate_id": cl.associate_id,
        "urgency": helpers.urgency(client_uuid),
        "recomendations": helpers.recomendations(client_uuid)
    }
    if tab == 'client_info':
        profile['client_info'] = [
            {
                "name": "first_name",
                "type": "text",
                "value": cl.first_name,
                "options": None
            },
            {
                "name": "last_name",
                "type": "text",
                "value": cl.last_name,
                "options": None
            },
            {
                "name": "middle_name",
                "type": "text",
                "value": cl.middle_name,
                "options": None
            },
            {
                "name": "social_security",
                "type": "text",
                "value": cl.social_security,
                "options": None
            },
            {
                "name": "date_of_birth",
                "type": "date",
                "value": cl.date_of_birth,
                "options": None
            },
            {
                "name": "ethnicity",
                "type": "select",
                "value": cl.ethnicity,
                "options": value_maps.race
            },
            {
                "name": "gender",
                "type": "select",
                "value": cl.gender,
                "options": value_maps.gender
            },
            {
                "name": "veteran",
                "type": "select",
                "value": cl.veteran,
                "options": value_maps.general_boolean_numbers
            }
        ]
    if tab == "employment_education":
        profile['employment_education'] = [
            {
                "name":"employed",
                "type": "select",
                "value": e.employed,
                "options": value_maps.general_boolean_numbers
            },
            {
                "name":"employment_type",
                "type": "select",
                "value": e.employment_type,
                "options": value_maps.employment_type
            },
            {
                "name":"not_employed_reason",
                "type": "select",
                "value": e.not_employed_reason,
                "options": value_maps.not_employed_reason
            },
            {
                "name":"last_grade_completed",
                "type": "select",
                "value": e.last_grade_completed,
                "options": value_maps.last_grade_completed
            }
        ]

    if tab == 'health_and_dv':
        profile['health_and_dv'] = [
            {
                "name":"domestic_violence_victim",
                "type":"select",
                "value": health.domestic_violence_victim,
                "options": value_maps.general_boolean_numbers
            },
            {
                "name": "when_occured",
                "type": "select",
                "value": health.when_occured,
                "options": value_maps.when_experience_occured
            },
            {
                "name": "currently_fleeing",
                "type": "select",
                "value": health.currently_fleeing,
                "options": value_maps.general_boolean_numbers
            },
            {
                "name": "general_health_status",
                "type": "select",
                "value": health.general_health_status,
                "options": value_maps.general_status
            },
            {
                "name": "dental_health_status",
                "type": "select",
                "value": health.dental_health_status,
                "options": value_maps.general_status
            },
            {
                "name": "mental_health_status",
                "type": "select",
                "value": health.mental_health_status,
                "options": value_maps.general_status
            },
            {
                "name": "pregnancy_status",
                "type": "select",
                "value": health.pregnancy_status,
                "options": value_maps.general_boolean_numbers
            },
            {
                "name": "due_date",
                "type": "date",
                "value": health.due_date,
                "options": None
            }
        ]

        if tab == 'service_recieved':
            profile['service_recieved'] = []
            for s in services:
                try:
                    profile['services_recieved'].append({
                        "name": value_maps.services_record_type[s.record_type]
                        "type": "read-only",
                        "value": value_maps.services_record_type_to_provided[s.record_type][s.type_provided]
                    })
                except:
                    continue



    return JsonResponse(profile)
