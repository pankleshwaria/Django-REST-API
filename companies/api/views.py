from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from companies.models import Stock
from companies.api.serializers import StockSerializer


# Create your views here.
# api/stocks/
@api_view(['GET', ])
def api_get_stocks_list(request):

    try:
        stocks = Stock.objects.all()
    except Stock.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


# Update the stock info
# api/stocks/<ticker>/
@api_view(['PUT', ])
def api_update_stock(request, ticker):

    try:
        stock = Stock.objects.get(ticker= ticker)
    except Stock.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {}
    if request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Updated successfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete stock
# /api/stock/delete/<ticker>
@api_view(['DELETE', ])
def api_delete_stock(request, ticker):

    try:
        stock = Stock.objects.get(ticker=ticker)
    except Stock.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = stock.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete failed"
        return Response(data=data)


# Create stock
# /api/stock/create/
@api_view(['POST', ])
def api_create_stock(request):

    if request.method == 'POST':
        stock = Stock()
        print()
        print(request.data)
        print()
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
