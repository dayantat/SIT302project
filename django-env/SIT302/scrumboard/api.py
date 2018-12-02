# from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ListSerializer, CardSerializer
from .models import List, Card


class ListViewSet(ModelViewSet):  # ModelViewSet handles all rest calls
    queryset = List.objects.all()  # This queries all list objects this is done in python and converted to JSON
    serializer_class = ListSerializer  # This handles the data as JSON by calling the ListSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

