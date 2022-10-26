from django.contrib import admin
from .models import Contacto

class AdminContacto(admin.ModelAdmin):
	list_display = ["nombres","apellidos","email"]
	class Meta(object):
		model = Contacto
admin.site.register(Contacto,AdminContacto)