from django.shortcuts import render, redirect
from .models import Objetivo
from .forms import ObjetivoForm, NewRegister


# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def subirobjetivo(request):
    if request.method=="POST":
        form = ObjetivoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user.username
            instance.save()
            return redirect("dashboard")
    else:
        form=ObjetivoForm()
    return render(request, 'subirobjetivo.html',{
        'form':form
    })

def verobjetivo(request):
    lista_objetivo= Objetivo.objects.all()
    return render(request, 'verobjetivo.html', {
        'lista_objetivo': lista_objetivo
    })

def indexView(request):
    return render(request,'index.html')

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form = NewRegister()
    
    return render(request,'registration/register.html',{'form':NewRegister})
