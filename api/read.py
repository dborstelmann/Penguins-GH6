import datetime
from django.http import JsonResponse
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from api.models import ( Applicant, Client, Disabilities, EmploymentEducation,
    Enrollment, HealthAndDV, IncomeBenefits, Services )

def get_applicants(request):

    applicant = {}

    return JsonResponse(applicant)

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
        "ethnicity":  1,
        "gender": 1,
        "veteran": 1,
        "year_entered": c.year_entered,
        "year_exited": c.year_exited,
        "date_created": c.date_created
    } for c in clients], safe=False)

def get_applicants(request):
    app_list = Applicant.objects.all()

    applicant = [{
        "first_name": c.first_name,
        "last_name": c.last_name,
        "why": c.why,
        "phone": c.phone,
        "email": c.emial,
        "address": c.address,
        "birthday": c.birthday,
        "ethnicity": ethnicity[c.ethnicity],
        "gender": gender[c.gender],
        "veteran": veteran[c.veteran],
        "family": c.family,
        "domestic_violence": domestic_violence[c.domestic_violence],
        "pregnancy": c.pregnancy,
        "drug": c.drug,
        "urgency": c.urgency,
        "created": c.created,
        "reviewed": c.reviewed

        } for c in app_list]

    return JsonResponse(applicant, safe=False)
