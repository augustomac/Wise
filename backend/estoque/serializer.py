from rest_framework import serializers
from estoque.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'nome', 'quantidade', 'valor']