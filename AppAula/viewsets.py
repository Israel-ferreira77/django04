from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework import viewsets

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    