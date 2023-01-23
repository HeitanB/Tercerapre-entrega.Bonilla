from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Equipo, DT
from AppCoder.forms import EquipoFormulario, DTFormulario

# Create your views here.

def Equipo(request):

      equipo =  Equipo(nombre="Barcelona FC")
      equipo.save()
      documentoDeTexto = f"--->Equipo: {equipo.nombre}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")



def jugadores(request):

      return render(request, "AppCoder/jugadores.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


def equipos(request):

      if request.method == 'POST':

            miFormulario = EquipoFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  equipos = Equipo (nombre=informacion['Equipo']) 

                  equipos.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= EquipoFormulario() 

      return render(request, "AppCoder/equipos.html", {"miFormulario":miFormulario})




def dt(request):

      if request.method == 'POST':

            miFormulario = DTFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  dt = DT (nombre=informacion['nombre'], club=informacion['club']) 

                  dt.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= DTFormulario()

      return render(request, "AppCoder/DT.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["jugador"]:

	      
            club = request.GET['club'] 
            equipos = Equipo.objects.filter(club__icontains=club)

            return render(request, "AppCoder/inicio.html", {"equipos":equipos, "club":club})

      else: 

	      respuesta = "No se insertaron datos"
      
      return HttpResponse(respuesta)