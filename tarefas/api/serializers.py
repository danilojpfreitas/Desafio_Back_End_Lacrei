from dataclasses import fields
import imp
from multiprocessing.pool import IMapUnorderedIterator
from rest_framework import serializers
from tarefas.models import Tarefas

class TarefasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = "__all__"