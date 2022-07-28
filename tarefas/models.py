from django.db import models
from uuid import uuid4

# Create your models here.

class Tarefas(models.Model):
    id_tarefa = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    nome_usuario = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
