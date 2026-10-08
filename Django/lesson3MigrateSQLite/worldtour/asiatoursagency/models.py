from django.db import models

# Create your models here.
class Tour(models.Model):
    #país de origem, destino, numero de noites e preço
   
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nigths = models.IntegerField()
    price = models.IntegerField()

    # Representacao em String dos Tours

    def __str__(self):
        return(f"ID:{self.id}: From {self.origin_country} To {self.destination_country}, {self.number_of_nigths} nights costs ${self.price}")