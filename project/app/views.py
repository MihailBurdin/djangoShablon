from django.shortcuts import render
from django.http import HttpResponse

def index(request):


    data = {
		"PlaceOfSudy": "Алабуга Политех",
		"Group": "Python 1",
		"Specialization": "Младший специалист",
		"InfoForMe": "Хочу стать продвинутым программистом"
	}
    return render(request, "index.html", context=data)

def about(request):

    data = {
		"FIO": "Бурдин Михаил Павлович",
		"Height": 182,
		"Weight": 70,
		"Age": 16
	}
    return render(request, "about.html", context=data)

def contacts(request):

    data = {
		"Номер телефона:": "+79962911378",
		"Телеграмм:": "@MihailAGH",
	}
    return render(request, "contacts.html", {"data": data.keys(), "values": data.values()})

def form(request):
    return render(request, "form.html")