from django.db import models

class Director(models.Model):
    FIO=models.CharField(max_length=100)
    dataAge=models.DateTimeField()

    def __str__(self):
        return self.FIO

class Genre(models.Model):
    nameGanre=models.CharField(max_length=30)

    def __str__(self):
        return self.nameGanre


class Afish(models.Model):
    data=models.DateTimeField()
    film=models.CharField(max_length=30)

class Film(models.Model):
    name = models.CharField(max_length=30)
    years = models.DateTimeField()
    country = models.CharField(max_length=40)
    director = models.ForeignKey(Director,on_delete= models.CASCADE,null=True)
    genre = models.ForeignKey(Genre,on_delete= models.CASCADE,null=True)

    def __str__(self):
        return self.name

