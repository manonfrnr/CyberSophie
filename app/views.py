from django.shortcuts import render, Http404
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

def stats(request):
    if not request.user.is_authenticated:
        return Http404("Not found")
    labels = []
    data = []

    responses = Reponse.objects.filter(question__id=1)
    choix = Choix.objects.filter(question__id=1)
    sum = {}
    for c in choix:
        sum[c.id] = 0
        labels.append(c.valeur)
    for r in responses:
        sum[int(r.valeur)] += 1
    for k, v in sum.items():
        data.append(v)

    return render(request, 'app/stats.html', {
        'labels': labels,
        'data': data,
    })
