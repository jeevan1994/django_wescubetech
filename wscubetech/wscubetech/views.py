from django.http import HttpResponse
from django.shortcuts import render
from .forms import  userForms
from service.models import Service


def aboutUS(request):
    return HttpResponse("Welcome to Wsbcubetech")


def Home(request):
    return render(request, "index.html")


def inner_page(request):
    return render(request, "inner-page.html")


def contact_us(request):
    form =userForms
    try:
        no1 = request.POST['no1']
        no2 = request.POST['no2']
        print(no1+no2)
    except:
        pass
    return render(request, "form.html",{'form':form})


def portfolio_details(request):
    return render(request, "portfolio-details.html")


# dynamic routing
def courses(request):
    return HttpResponse("Course")


def course(request, id):
    servicedata = Service.objects.all()
    if id == 1:
        course_details = "java course"
    elif id == 2:
        course_details = "python course"
    else:
        course_details = "other course"
    data = {
        'title': course_details,
        'service':servicedata
    }
    print(servicedata)
    for servicedata in servicedata:
        print(servicedata.service_icon)
    return render(request, "course.html", data)
