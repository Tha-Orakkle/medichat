from django.shortcuts import render
from . import ingestion_time

# Create your views here.

def index(request):
    context = {
            'ingestion_time': f"{ingestion_time:.4f}"
    }
    return render(request, 'index.html', context)
