from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Mosque, Lga

# Create your views here.

def home(request):
    cities = Lga.objects.all()
    mosques = Mosque.objects.all()
    context = {
        'cities': cities,
        'mosques': mosques
        }
    return render(request, 'home.html', context)


def apply(request):
    name_id = request.GET.get('mosque')
    name = get_object_or_404(Mosque.objects.prefetch_related('name'), name__id=name_id)
    context = {'mosque': name}
    return render(request, 'apply.html', context)