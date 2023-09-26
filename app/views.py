from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
def registration(request):
    USFO=UserForm()
    PFO=ProfileForm()
    d={'USFO':USFO,'PFO':PFO}
    return render(request,'registration.html',d)