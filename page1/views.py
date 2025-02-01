from django.shortcuts import render
from .models import users


def store_data(request):

    if request.method == "POST":
        _username = request.POST.get("username")
        _password = request.POST.get("password")
        if users.objects.filter(username=_username).exists():
            error = {"error":"username is already exist"}
            return render(request,'page1/form1.html',error)
        else:
            data = users(username=_username, password=_password)
            data.save()
    return render(request,'page1/form1.html')
# Create your views here.
