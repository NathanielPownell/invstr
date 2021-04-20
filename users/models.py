from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import requests
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=100000)


@receiver(post_save, sender=User)
def create_or_update_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
    instance.account.save()
    
class Position(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    entryprice = models.FloatField()
    exitprice = models.FloatField(blank=True)
    symbol = models.CharField(max_length=10)

    def getPrice(symbol):
        return (str(requests.get('https://finnhub.io/api/v1/quote?symbol={symbol}&token=c1nom4i37fkph7jrlvdg').json()['c']))


    def __str__(self):
        return self.entry



        
class Wlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    symbol = models.CharField(max_length=9, blank=True)


    # for x in symbols:
    #     prices.append(str(requests.get('https://finnhub.io/api/v1/quote?symbol={symbol}&token=c1nom4i37fkph7jrlvdg').json()['c']))
    
    

    class Meta:
            ordering = ["id"] #ordering by the created field

    def __str__(self):
        return self.symbol



    def get_absolute_url(self):
        return reverse('watchlistedit')
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wlist = models.OneToOneField(Wlist, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)