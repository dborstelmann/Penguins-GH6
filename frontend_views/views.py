from django.template.response import TemplateResponse
from utils.custom_decorators import login_required


def base_view(request):
    # if not request.user.is_authenticated():
    #     return TemplateResponse(request, 'base/404.html', {})

    return TemplateResponse(request, 'hello.html', {})


def apply_view(request):
    return TemplateResponse(request, 'apply.html', {})


@login_required
def home_view(request):
    return TemplateResponse(request, 'home.html', {})


def submit_view(request):
    return TemplateResponse(request, 'submit.html', {})
