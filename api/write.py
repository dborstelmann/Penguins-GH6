from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


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
    return JsonResponse({'data': 'success'})
