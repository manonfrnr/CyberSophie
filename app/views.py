from django.shortcuts import render, Http404
from django.utils import timezone
from .models import *

# Create your views here.
def sondage(request):
    return render(request, 'app/sondage.html', {'questions': Question.objects.all(), "choix": Choix.objects.all()})

def resultat(request):
    print(request.POST)
    for k,v in request.POST.items():
        if k == 'csrfmiddlewaretoken':
            print("token")
            continue
        try:
            print(k, v)
            q = Question.objects.get(id=k)
            try:
                c = Choix.objects.get(id=v)
                if c.question != q:
                    print(q, v, "not found")
                    continue
            except ValueError:
                if not q.isLibre:
                    print(q, v, "libre not found")
                    continue
            r = Reponse(question=q, valeur=v)
            r.save()
        except:
            continue
    return render(request, 'app/sondage.html', {"ok": "ok"})

def stats(request):
    if not request.user.is_authenticated:
        return Http404("Not found")
    labels = []
    data = []

    question_id = 1
    start_date = timezone.now() - timezone.timedelta(days=1)
    end_date = timezone.now()
    question = Question.objects.get(id=question_id)
    if not question.isLibre:
        responses = Reponse.objects.filter(question=question, date__lt=end_date, date__gt=start_date)
        choix = Choix.objects.filter(question=question)
        sum = {}
        for c in choix:
            sum[c.id] = 0
            labels.append(c.valeur)
        for r in responses:
            sum[int(r.valeur)] += 1
        for k, v in sum.items():
            data.append(v)

        return render(request, 'app/stats.html', {
            'start_date': start_date,
            'end_date': end_date,
            'question': question,
            'labels': labels,
            'data': data,
        })
    else:
        responses = Reponse.objects.filter(questio=question, date__lt=end_date, date__gt=start_date)
        return render(request, 'app/stats.html', {
            'start_date': start_date,
            'end_date': end_date,
            'question': question,
            'reponses': responses,
        })
