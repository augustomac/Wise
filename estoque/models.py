from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
    nome = models.CharField(max_length=60)
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    valor = models.FloatField(validators=[MinValueValidator(0)],)

    def __str__(self):
        return self.nome
