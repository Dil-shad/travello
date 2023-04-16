from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def index(request):
    obj=Destination.objects.all()
    obj_teams=Teams.objects.all()
    try:
        user_name=request.user
    except:
        pass
    return render(request,'index.html',{'obj':obj,'obj_teams':obj_teams,'uname':user_name})
