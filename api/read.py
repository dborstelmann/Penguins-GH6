import datetime
from django.http import JsonResponse
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from api.models import ( Applicant, Client, Disabilities, EmploymentEducation,
    Enrollment, HealthAndDV, IncomeBenefits, Services, ContinuumServices )

from utils import value_maps

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
            clients = clients.filter(last_name__contains=q)


    return JsonResponse([{
        "first_name": c.first_name,
        "middle_name": c.middle_name,
        "last_name": c.last_name,
        "social_security": c.social_security,
        "date_of_birth": datetime.datetime.strftime(c.date_of_birth, '%m/%d/%Y'),
        "ethnicity":  value_maps.ethnicity[c.ethnicity],
        "gender": value_maps.gender[c.gender],
        "veteran": value_maps.veteran[c.veteran],
        "year_entered": c.year_entered,
        "year_exited": c.year_exited,
        "date_created": c.date_created,
        "id": c.uuid
    } for c in clients], safe=False)

def get_applicants(request):
    app_list = Applicant.objects.all()

    applicant = [{
        "id": c.id,
        "first_name": c.first_name,
        "last_name": c.last_name,
        "why": c.why,
        "phone": c.phone,
        "email": c.emial,
        "address": c.address,
        "birthday": c.birthday,
        "ethnicity": value_maps.ethnicity[c.ethnicity],
        "gender": value_maps.gender[c.gender],
        "veteran": value_maps.veteran[c.veteran],
        "family": c.family,
        "domestic_violence": value_maps.domestic_violence[c.domestic_violence],
        "pregnancy": c.pregnancy,
        "drug": c.drug,
        "urgency": c.urgency,
        "created": c.created,
        "reviewed": c.reviewed,
        "recomendations": ContinuumServices.objects.reccomendations(c)
        } for c in app_list]

    return JsonResponse(applicant, safe=False)

def profile(request):
    client_uuid = request.POST['id']
    cl = Client.objects.filter(uuid=client_uuid).first()
    if c is None:
        return {"status": "error", "message": "member not found"}
