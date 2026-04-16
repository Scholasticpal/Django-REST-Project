from django.shortcuts import render, HttpResponse
from datetime import datetime
from homeApp.models import Contact
from django.contrib import messages


def index(request):
    context = {
        "name": "Anmol"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
    return render(request, 'contact.html')

