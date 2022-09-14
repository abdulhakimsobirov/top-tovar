from rest_framework import serializers
from .models import Category, Product, Request


class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(method_name='get_image_url')

    class Meta:
        model = Category
        fields = [
             'name', 'image_url', 'count'
        ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(method_name='get_image_url')


    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price','image_url', 'video', 'top']
        depth = 1
    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'client_name', 'phone', 'region'
        ]

