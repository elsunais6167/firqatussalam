from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def landing(request):

    context = {

    }

    return render(request, 'index.html', context)


def my_view(request):
    url = reverse('itikaf:login')