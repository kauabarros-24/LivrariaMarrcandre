from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora, Autor
from livraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer