

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Category, Product, Request
from .serializers import ProductSerializer, CategorySerializer, RequestSerializer
from config.mixins import ListAPIViewResponseMixin, RetrieveAPIViewResponseMixin, CreateAPIViewResponseMixin, \
    UpdateAPIViewResponseMixin, DestroyAPIViewResponseMixin
# Create your views here.

# --------------------------------------Product------------------------------------------

class BaseProductView:
    queryset = Product.objects.all()


class ProductListView(BaseProductView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['name']
    search_fields = ['name']
    # field = 'name'

class ProductView(BaseProductView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = ProductSerializer

class ProductCreateView(BaseProductView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = ProductSerializer

class ProductUpdateView(BaseProductView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = ProductSerializer

class ProductDeleteView(BaseProductView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass


# ----------------------------------------------Category--------------------------------------

class BaseCategoryView:
    queryset = Category.objects.all()


class CategoryListView(BaseCategoryView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['name']
    search_fields = ['name']
    # field = 'name'

class CategoryView(BaseCategoryView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = CategorySerializer


# ---------------------------------------------Request-----------------------------------------


class BaseRequestView:
    queryset = Request.objects.all()


# class CategoryListView(BaseCategoryView, ListAPIViewResponseMixin, generics.ListAPIView):
#     serializer_class = CategorySerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filter_fields = ['name']
#     search_fields = ['name']
#     # field = 'name'

class RequestView(BaseRequestView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = RequestSerializer


class RequestCreateView(BaseRequestView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = RequestSerializer
