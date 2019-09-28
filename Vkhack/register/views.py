from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from json_parse.main import *
from django.http import JsonResponse

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
 
def register(request):
    form = RegisterForm()
    museum = base_navigation()
    print(request)
    context = {}
    if request.method == "GET":
        form = RegisterForm(request.GET) #if no files
        if form.is_valid():
            context = {
                'form': form
            }
    return JsonResponse(museum.objects.get_list_objects(), safe=False)