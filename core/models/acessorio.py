from django.db import models


class Acessorio(models.Model):
    descricao = models.Cherfield(max_length = 100)