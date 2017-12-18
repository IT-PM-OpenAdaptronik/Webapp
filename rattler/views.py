from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
#from apps.process import forms as ProcessForms

@login_required
def dashboard (request):
    return render(
        request,
        'dashboard/index.html',
        #{
        #    'upload_form': ProcessForms.UploadFileForm()
        #}
    )

def error404 (request):
    return render (request,'error404/index.html')

@login_required
def community (request):
    return render (request,'community/index.html')

@login_required
def profileMe (request):
    return render (request,'profile/me/index.html')

@login_required
def admin (request):
    return render (request,'admin/index.html')

@login_required
def settings (request):
    return render (request,'settings/index')

@login_required
def help (request):
    return render (request,'help/index.html')

def index(request):
    if not request.user.is_authenticated:
        return render(
            request,
            'index/index.html',
            {
                'login_form': AuthenticationForm()
            }
        )
    else:
        return render(request, 'dashboard/index.html')

