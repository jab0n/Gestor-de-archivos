from django.shortcuts import render, redirect
from .forms import MultipleFileUploadForm
from .models import Archivo

def subir_archivos(request):
    if request.method == "POST":
        form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivos = form.cleaned_data["archivos"]
            for archivo in archivos:
                Archivo.objects.create(archivo=archivo)
            return redirect("lista_archivos")
    else:
        form = MultipleFileUploadForm()

    return render(request, "uploads/subir.html", {"form": form})

def lista_archivos(request):
    archivos = Archivo.objects.all()
    return render(request, "uploads/lista.html", {"archivos": archivos})