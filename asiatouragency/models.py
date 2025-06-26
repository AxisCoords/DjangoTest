from django.db import models

class Tour(models.Model):
    originCountry = models.CharField(max_length=64)
    destinationCountry = models.CharField(max_length=64)
    numberOfNights = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id}, Origin: {self.originCountry}, Destination: {self.destinationCountry}, NumOfNights: {self.numberOfNights}, Price: ${self.price}"
