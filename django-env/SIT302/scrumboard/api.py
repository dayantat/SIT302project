from rest_framework.viewsets import ModelViewSet
from .serializers import ListSerializer, CardSerializer
from .models import List, Card
from rest_framework import permissions


class ListViewSet(ModelViewSet):  # ModelViewSet handles all rest calls
    queryset = List.objects.all()  # This queries all list objects this is done in python and converted to JSON
    serializer_class = ListSerializer  # This handles the data as JSON by calling the ListSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)
