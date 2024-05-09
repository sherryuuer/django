from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ItemSerializer
from .models import Item


# Create your views here.
# def item_list(request):
#     # QueryObj -> Python List[dict]
#     items = []
#     for item in Item.objects.all():
#         items.append({
#             'name': item.name,
#             'price': item.price,
#             'description': item.description,
#         })
#     return JsonResponse({'menu_items': items})

# rewrite the function
@api_view(['GET'])
def item_list(request):
    serializer = ItemSerializer(Item.objects.all(), many=True)
    return Response(serializer.data)


def item_list_serialized(request):
    serializer = ItemSerializer(Item.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
