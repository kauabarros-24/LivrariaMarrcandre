from django.contrib import admin

from livraria.models import Categoria, Editora, Autor

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
