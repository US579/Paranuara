from django.db import models

class Company(models.Model):
    index = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=50)
    def __str__(self):
        return self.company

class People(models.Model):
    _id = models.CharField(max_length=50)
    index = models.IntegerField(primary_key=True)
    guid = models.CharField(max_length=50)
    has_died = models.BooleanField(default=False)
    picture = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age = models.IntegerField(null=True)
    eyeColor = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    company_id = models.ForeignKey(Company,
                                   related_name='employees',
                                   on_delete=models.PROTECT,
                                   null=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    tags = models.CharField(max_length=50, default="")
    about = models.CharField(max_length=500)
    registered = models.CharField(max_length=50)
    greeting = models.CharField(max_length=100, default="")
    fruits = models.CharField(max_length=100, default="")
    vegetables = models.CharField(max_length=100, default="")
    friends = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
