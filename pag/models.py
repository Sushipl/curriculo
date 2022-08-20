from datetime import datetime
from django.db import models

class Avaliacao(models.Model):
    veri = models.BooleanField(default=False)
    nome = models.CharField(max_length=150)
    agora = models.DateField()
    texto = models.TextField()
    img = models.ImageField(upload_to='imagens/', blank=True)
    def __str__(self):
        return self.nome