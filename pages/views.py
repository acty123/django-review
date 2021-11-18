from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse('<h1>Hello Peter<h1>')
    return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_name": "example name",
        "phone": 1234567,
        "address": "calle 1 #12-22",
        "my_list": [123,234,543,"txt"]  
    }
    return render(request, "contact.html", my_context)
