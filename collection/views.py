from django.shortcuts import render
from collection.models import Loonatic

def index(request):
    loonatics = Loonatic.objects.all()
    return render(request, 'index.html', {'loonatics': loonatics,})
