from django.shortcuts import render
from .models import *

# Create your views here.
def sondage(request):
    return render(request, 'app/sondage.html', {'questions': Question.objects.all(), "choix": Choix.objects.all()})