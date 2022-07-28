from rest_framework import viewsets
from tarefas.api.serializers import TarefasSerializers
from tarefas.models import Tarefas

class TarefasViewSet(viewsets.ModelViewSet):
    serializer_class = TarefasSerializers
    queryset = Tarefas.objects.all()