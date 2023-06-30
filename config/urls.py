from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import AutorViewSet, CategoriaViewSet, EditoraViewSet

router = DefaultRouter()
router.register(r"autores", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]