from rest_framework.generics import ListAPIView

from .serializers import ListSerializer, CardSerializer
from .models import List, Card

class ListApi(ListAPIView):  # This inheritets from ListAPIView
    queryset = List.objects.all()  # This queries all list objects this is done in python and converted to JSON
    serializer_class = ListSerializer  # This handles the data as JSON by calling the ListSerializer

class CardApi(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer