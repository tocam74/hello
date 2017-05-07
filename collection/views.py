from django.shortcuts import render, redirect
from collection.models import Loonatic
from collection.forms import LoonaticForm

def index(request):
    loonatics = Loonatic.objects.all()
    return render(request, 'index.html', {'loonatics': loonatics,})

def loonatic_detail(request, slug):
    loonatic = Loonatic.objects.get(slug=slug)
    return render(request, 'loonatics/loonatic_detail.html', {'loonatic': loonatic,})

def edit_loonatic(request, slug):
    loonatic = Loonatic.objects.get(slug=slug)
    form_class = LoonaticForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=loonatic)
        if form.is_valid():
            form.save()
            return redirect('loonatic_detail', slug=loonatic.slug)
    else:
        form = form_class(instance=loonatic)
    return render(request, 'loonatics/edit_loonatic.html', {'loonatic': loonatic, 'form': form,})
