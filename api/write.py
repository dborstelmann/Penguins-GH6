from django.http import JsonResponse
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from api.models import ( Applicant, Client, Disabilities, EmploymentEducation,
    Enrollment, HealthAndDV, IncomeBenefits, Services )


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

    return JsonResponse({'status': 'success'})

def mark_reviewed(request):
    '''
        request.POST =
            applicant_id
    '''

    return JsonResponse({'status': 'success'})

def get_applicants(request):

    applicant = {}

    return JsonResponse(applicant)

def search_clients(request):
    pass
