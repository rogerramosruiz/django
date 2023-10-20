from django.shortcuts import render, redirect
from .models import Corredor
from .forms import CorredorForm

# Create your views here.
def listar_corredores(request):
    por = request.GET.get('por')
    orden_por = ('codigo', 'nombreCompleto', 'comision', 'codigoAPS')
    corredores = Corredor.objects.filter(isActive=1)
    if por in orden_por:
        corredores = corredores.order_by(por)
    return render(request, 'list.html', context={'corredores': corredores})


def detalle_corredor(request, pk):
    corredor =Corredor.objects.get(pk = pk)
    return render(request, 'detail.html', context={'corredor': corredor})


def crear_corredor(request):
    form = CorredorForm()
    if request.method == 'POST':
        form = CorredorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'form.html', context={'form': form})


def actualizar_corredor(request, pk):
    corredor = Corredor.objects.get(pk = pk)
    form = CorredorForm(request.POST or None, instance = corredor)
    if request.method == 'POST':
            form.save()
            return redirect('home')
        
    return render(request, 'form.html', context={'form': form})

def eliminar_corredor(request, pk):
    corredor = Corredor.objects.get(pk = pk)
    corredor.isActive = 0
    corredor.save()
    return redirect('home')