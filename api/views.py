from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cached_item = cache.get(f'item_{item_id}')
        if cached_item:
            return Response(cached_item)
        
        response = super().retrieve(request, *args, **kwargs)
        cache.set(f'item_{item_id}', response.data)
        return response

