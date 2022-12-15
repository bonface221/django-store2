from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product,Collection
from .serializers import ProductSerializer,CollectionSerializer

# Create your views here.
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related(
        'collection').all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self,request):
        obj = self.get_object()
        if obj.orderitem_set.count() > 0:
            return Response(
                {'error': 'Product cannot be deleted because it is associated with an order Item'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer


class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def delete(self,request,pk):
        obj = self.get_object()
        if obj.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products'})
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

