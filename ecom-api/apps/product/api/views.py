from django.http import Http404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProductSerializer, CategorySerializer
from ..models import Product, Category
from ...commons.utils.auth import JwtAuthentication


class FetchCategories(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def get_category(self, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404

    @action(detail=False, methods=['get'])
    def category_details(self, request):
        query_params = request.query_params
        category_slug = query_params['category_slug']
        queryset = self.get_category(category_slug)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)


class FetchLatestProducts(viewsets.ViewSet):

    def list(self, request):
        # queryset = Product.objects.all()[:4][:4]
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def product_details(self, request):
        query_params = request.query_params
        try:
            category_slug = query_params['category_slug']
            product_slug = query_params['product_slug']
            queryset = Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
            serializer = ProductSerializer(queryset)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404


class Search(viewsets.ViewSet):

    def getProduct(self, query):
        try:
            return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        except Product.DoesNotExist:
            raise Http404
        ...

    @action(detail=False, methods=['post'])
    def search(self, request):
        query = request.data.get('query')
        products = self.getProduct(query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
