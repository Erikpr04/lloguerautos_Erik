from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)

    def __str__(self):
        return self.marca+" "+self.model+" "+self.matricula
    
class Reserva(models.Model):
    data_inici = models.DateField()
    data_fi = models.DateField(blank=True,null=True)
    cotxe = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    usuari = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        unique_together = ('data_inici', 'cotxe') 

    def __str__(self):
        return f"Reserva de {self.cotxe} el {self.data_inici}"



