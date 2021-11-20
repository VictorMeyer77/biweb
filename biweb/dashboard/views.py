from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BMO
import json

def index(request):
    template = loader.get_template('dashboard/index.html')
    return HttpResponse(template.render(request=request))

def charts(request):
    template = loader.get_template('dashboard/charts.html')
    context = {
        "data": json.dumps({"data": [0, 10000, 65000, 15000, 90000, 20000, 15000, 25000, 78000, 30000, 25000, 40000]})
    }
    return HttpResponse(template.render(context, request=request))

def listVille(request, limit):
    villes = BMO.objects.all()[:int(limit)]
    formatted_villes = ["<li>{}</li>".format(ville.nom_be21) for ville in villes]
    message = """<ul>{}</ul>""".format("\n".join(formatted_villes))
    return HttpResponse(message)

