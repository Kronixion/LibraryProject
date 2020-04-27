from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=70)
    coverImage = models.ImageField(upload_to='books/')
    description = models.TextField()
    yearOfRelease = models.DateField()
    price = models.IntegerField()
    rental = models.BooleanField()
    exchange = models.BooleanField()
    publisher = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=20)

    def __str__(self):
        return self.title