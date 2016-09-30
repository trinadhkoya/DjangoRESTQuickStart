from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Stock
from app.serializers import StockSerializer



class StockList(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


