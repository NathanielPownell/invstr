  
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import requests


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



# class User(models.Model):



class Stock(models.Model):

    

    title=models.CharField(max_length=50)
    
    # def getprice(symbol):
    #     r = requests.get('https://finnhub.io/api/v1/quote?symbol={}&token=##############'.format(str(symbol)))

    #     quote = r.json()["c"]

    #     return quote
    
    def __str__(self):
        return f"{self.title}"
    
    # price = models.CharField(max_length=10, default=getprice(title))

    

    
    


class Watchlist(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ManyToManyField(Stock)
#    price = models.ManyToManyField(Stock.price)
   def __str__(self):
       return f"{self.user}'s WatchList" 