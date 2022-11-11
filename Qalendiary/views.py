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
            instance.usuario = request.user.id
            instance.save()
            return redirect("verobjetivo")
    else:
        form=ObjetivoForm()
        try:
            dia=request.GET["d"]
            mes= request.GET["m"]
            anio=request.GET["y"]
            fecha=anio+'-'+mes+'-'+dia
        except:
            fecha='' 
        return render(request, 'subirobjetivo.html',{
        'form':form,
        'fecha':fecha,
    })

def verobjetivo(request):
    try:
        dia=request.GET["d"]
        mes= request.GET["m"]
        anio=request.GET["y"]
        lista_objetivo= Objetivo.objects.filter(usuario=request.user.id,fecha_obj__day=dia, fecha_obj__month=mes, fecha_obj__year=anio)
        return render(request, 'verobjetivo.html',{
            'lista_objetivo': lista_objetivo,
            'Hola':'confecha',
            'dia':dia,
            'mes':mes,
            'anio':anio

        })
    except:
        lista_objetivo= Objetivo.objects.filter(usuario=request.user.id)
        return render(request, 'verobjetivo.html',{
            'lista_objetivo': lista_objetivo,
            'Hola':'sinfecha'
        })
    #print(dia)
    #lista_objetivo= Objetivo.objects.filter(usuario=request.user.id,fecha='2022-10-')
    #lista_objetivo= Objetivo.objects.filter(fecha__month=mes)
    #return render(request, 'verobjetivo.html', {
    #    'lista_objetivo': lista_objetivo,
    #    'Hola':'paseeee'
    #})

def borrarobjetivo(request, pk):
    if request.method == "POST":
        objetivo = Objetivo.objects.get(pk=pk)
        objetivo.delete()
    return redirect('verobjetivo')

def indexView(request):
    return render(request,'index.html')

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            #form = NewRegister()
            return render(request,'registration/register2.html',{'form':NewRegister})
    
    return render(request,'registration/register.html',{'form':NewRegister})

def calendarioView(request):
    return render(request,'calendario.html')

def temporizadorView(request):
    return render(request,'temporizador.html')



