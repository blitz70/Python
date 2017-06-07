from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Stock
from .my_rest_api import StockSerializer

# Create your views here.


class StockListView(APIView):

    def get(self, request):  # list
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):  # create
        pass
