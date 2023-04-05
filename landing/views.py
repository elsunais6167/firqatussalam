from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def landing(request, error_message=None):

    context = {

    }

    return render(request, 'index.html', context)
