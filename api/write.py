import datetime
import random
from django.http import JsonResponse
from dateutil.parser import parse
from utils import value_maps
from django.contrib.auth.decorators import login_required
from api.models import ( Applicant, Client, Disabilities, EmploymentEducation,
    Enrollment, HealthAndDV, IncomeBenefits, Services, ContinuumServices, Shelters )


def apply(request):
    """
        request.POST =
            first_name
            last_name
            why
            phone
            email
            address
            birthday
            race
            gender
            veteran
            enrolled_before
            family
            domestic_violence
            pregnancy
            drug
        }
    """
    a_dict = dict(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        why=request.POST['why'],
        phone=request.POST['phone'],
        email=request.POST['email'],
        address=request.POST['address'],
        birthday=parse(request.POST['birthday']),
        ethnicity=request.POST['race'],
        gender=request.POST['gender'],
        veteran=request.POST['veteran'],
        family=request.POST['family'],
        domestic_violence=request.POST['domestic_violence'],
        pregnancy=request.POST['pregnancy'],
        drug=request.POST['drug'],
    )
    app = Applicant(**a_dict)
    app.urgency = Applicant.objects.calculate_urgency(a_dict)
    app.reviewed = False
    a_dict['urgency'] = app.urgency
    app.save()

    return JsonResponse(ContinuumServices.objects.recomendations(app), safe=False)

def mark_reviewed(request):
    '''
        request.POST =
            id
    '''
    try:
        applicant = Applicant.objects.get(pk=request.POST['id'])
        applicant.reviewed = True
        applicant.save()
        return JsonResponse({'status': 'success'})

    except:
        return JsonResponse({'status': 'error'})

def update_shelter(request):
    '''
        request.POST =
            id
            occupancy
    '''
    try:
        shelters = Shelters.objects.get(pk=request.POST['id'])
        shelters.occupancy = request.POST['occupancy']
        shelters.last_updated = datetime.datetime.now()
        shelters.save()
        return JsonResponse({'status': 'success'})

    except:
        return JsonResponse({'status': 'error'})


def new_client(request):

    number = int(random.random()*1000000)
    while Client.objects.filter(uuid=number).exists():
        number = int(random.random()*1000000)

    Client(uuid=number).save()


    return JsonResponse({
        'status': 'success',
        'id': number
    })

def profile(request):
    '''
        request.POST =
            id
            name
            value
    '''
    client = Client.objects.filter(uuid=request.POST['id']).first()
    if client is None:
        return JsonResponse({"status": "error", "message": "Client not found"})

    e = EmploymentEducation.objects.filter(personal_id=request.POST['id']).first()
    health = HealthAndDV.objects.filter(personal_id=request.POST['id']).first()

    if hasattr(client, request.POST['name']):
        setattr(client, request.POST['name'], request.POST['value'])
        client.date_updated = datetime.datetime.now()
        client.associate_id = '245092'
        client.save()
        return JsonResponse({"status": "success"})

    if e is not None and hasattr(e, request.POST['name']):
        setattr(e, request.POST['name'], request.POST['value'])
        e.date_updated = datetime.datetime.now()
        e.associate_id = '245092'
        e.save()
        return JsonResponse({"status": "success"})

    if health is not None and hasattr(health, request.POST['name']):
        setattr(health, request.POST['name'], request.POST['value'])
        health.date_updated = datetime.datetime.now()
        health.associate_id = '245092'
        health.save()
        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error", "message": "attribute not found"})
