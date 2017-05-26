from django.shortcuts import render, redirect
from collection.models import Loonatic
from collection.forms import LoonaticForm, ContactForm
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    loonatics = Loonatic.objects.all()
    return render(request, 'index.html', {'loonatics': loonatics,})

def loonatic_detail(request, slug):
    loonatic = Loonatic.objects.get(slug=slug)
    return render(request, 'loonatics/loonatic_detail.html', {'loonatic': loonatic,})

@login_required
def edit_loonatic(request, slug):
    loonatic = Loonatic.objects.get(slug=slug)
    if request.user != loonatic.user:
        raise Http404
    form_class = LoonaticForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=loonatic)
        if form.is_valid():
            form.save()
            return redirect('loonatic_detail', slug=loonatic.slug)
    else:
        form = form_class(instance=loonatic)
    return render(request, 'loonatics/edit_loonatic.html', {'loonatic': loonatic, 'form': form,})

def create_loonatic(request):
    form_class = LoonaticForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            loonatic = form.save(commit=False)
            loonatic.user = request.user
            loonatic.slug = slugify(loonatic.name)
            loonatic.save()
            return redirect('loonatic_detail', slug=loonatic.slug)
    else:
        form = form_class()
    return render(request, 'loonatics/create_loonatic.html', {'form': form,})

def browse_by_name(request, initial=None):
    if initial:
        loonatics = Loonatic.objects.filter(name__istartswith=initial)
        loonatics = loonatics.order_by('name')
    else:
        loonatics = Loonatic.objects.all().order_by('name')

    return render(request, 'search/search.html', {'initial': initial, 'loonatics': loonatics,})

def contact(request):
    form_class = ContactForm

    return render(request, 'contact.html', {'form': form_class,})
