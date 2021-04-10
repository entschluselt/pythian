from django.shortcuts import render
from django.http import HttpResponse
from pythianapp.models import patients,med_data
# Create your views here.
def result(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("mail")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        symptoms = request.POST.get("symptoms")
        severity = request.POST.get("severe")
        days = request.POST.get("days")
        msz = request.POST.get("msz")
        patient = patients(name=name, email = email, age = age , gender = gender, symptoms=symptoms, severity=severity,days=days,msz=msz)
        patient.save()
    
    if request.method == "POST":
        sym = request.POST.get("symptoms")
        print(sym)
        sev = request.POST.get("severe")
        print(sev)
        med = med_data.objects.filter(data_symptoms=sym, data_severity=sev)
        print(med)
        context = {
            'medname':med
        }
    return render(request,'result.html', context)

def index(request):
    return render(request, 'index.html')