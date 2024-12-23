from rest_framework import serializers
from .models import Sell

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = ["user", "crypto_name", "crypto_amount", "timestamp"]
