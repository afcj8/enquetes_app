import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length = 200)
    data_pub = models.DateTimeField('Data de publicação')
    def __str__(self):
        return self.pergunta_texto
    def pub_recentemente(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(days = 1)
    def total_votos(self):
        total = 0
        for alt in self.alternativa_set.all():
            total += alt.votos
        return total

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete = models.CASCADE)
    alternativa_texto = models.CharField(max_length = 200)
    votos = models.IntegerField(default = 0)
    def __str__(self):
        return self.alternativa_texto
    def porcentagem(self):
        return (self.votos / self.pergunta.total_votos()) * 100