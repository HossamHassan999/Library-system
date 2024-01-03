from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)




    

