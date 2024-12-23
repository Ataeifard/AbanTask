from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Sell
from .serializers import SellSerializer


class SellListApiView(APIView):
    permission_classess = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        sells = Sell.objects.filter(user = request.user.id)
        serializer = SellSerializer(sells, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK )


    def post(self, request, *args, **kwargs):
        data = {
            'user': request.user.id,
            'crypto_name': request.data.get('crypto_name'),
            'crypto_amount': request.data.get('crypto_amount')
        }
        serializer = SellSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SellDetailApiView(APIView):
    permission_classess = [permissions.IsAuthenticated]