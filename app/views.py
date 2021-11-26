from django import db
from django.shortcuts import redirect, render
from app.forms import SureForm
from app.models import Sure
# Create your views here.

def home(request):
    data = {}
    data['db'] = Sure.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = SureForm()
    return render(request,'form.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Sure.objects.get(pk=pk)
    data['form'] = SureForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Sure.objects.get(pk=pk)
    form = SureForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Sure.objects.get(pk=pk)
    db.delete()
    return redirect('home')
    
def create(request):
    form = SureForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Sure.objects.get(pk=pk)
    return render(request, 'view.html', data)



