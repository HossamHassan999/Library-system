from django.db import models


class Tasnif(models.Model):


    Tasnif = models.CharField(max_length = 60)

    def __str__(self):
        return self.Tasnif
    

class Books(models.Model):

    name = models.CharField(max_length =100)
    
    Status =(

    ("متاح", "متاح"),
    ("تم بيعه", "تم بيعه"),
    ("مستعار", "مستعار"),

    )

    status =  models.CharField(
    max_length = 30,
    choices = Status,
    default = 'Available'

    )

    Author = models.CharField(max_length = 50)

    number_pages = models.IntegerField()

    price = models.IntegerField()

    category = models.ForeignKey( Tasnif , on_delete=models.CASCADE ,null=True, blank=True)

    image = models.ImageField(upload_to='images/' , null= True )

    def __str__(self):

        return self.name



    

