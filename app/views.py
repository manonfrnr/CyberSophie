from django.shortcuts import render
from .models import *

# Create your views here.
def sondage(request):
    return render(request, 'app/sondage.html', {'questions': Question.objects.all(), "choix": Choix.objects.all()})

def resultat(request):
    print(request.POST)
    for k,v in request.POST.items():
        if k == 'csrfmiddlewaretoken':
            continue
        print(k, v)
        r = Reponse(question = Question.objects.get(id=k), valeur=v)
        r.save()
    return render(request, 'app/sondage.html', {'questions': Question.objects.all(), "choix": Choix.objects.all()})