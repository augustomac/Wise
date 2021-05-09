from rest_framework import viewsets
from estoque.models import Item
from estoque.serializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
