from django.contrib import admin
from  .models import * #importamos el archivo models


admin.site.register(Equipo)

admin.site.register(Jugador)

admin.site.register(DT)

admin.site.register(Entregable)
