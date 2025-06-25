from django.db import models


# Create your models here.
class Meal(models.Model):
    # Nom des repas.
    name = models.CharField("Name of meal", max_length=100)

    # Description de notre repas
    # Champ facultatif
    description = models.TextField("Description of meal", blank=True, null=True)

    # Stocke le prix du repas.
    price = models.DecimalField("Price ($)", max_digits=10, decimal_places=2)

    # Disponible stocke le booléen vrai ou faux selon que le repas est disponible en ligne.
    available = models.BooleanField("Online Availability", default=False)

    # Comptage des stocks : compte le nombre de repas restants.
    stock = models.IntegerField("Stock Count", default=0)

    def __str__(self):
        return f"{self.description}"
