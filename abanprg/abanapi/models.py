from django.db import models
from django.contrib.auth.models import User


class Sell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    crypto_name = models.CharField(max_length = 40) 
    crypto_amount = models.SmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False, blank=True)

    def __str__(self):
        return(self.crypto_name)
