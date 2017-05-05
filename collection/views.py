from django.shortcuts import render
from collection.models import Loonatic

def index(request):
    loonatics = Loonatic.objects.all()
    return render(request, 'index.html', {'loonatics': loonatics,})

def loonatic_detail(request, slug):
    loonatic = Loonatic.objects.get(slug=slug)
    return render(request, 'loonatics/loonatic_detail.html', {'loonatic': loonatic,})
