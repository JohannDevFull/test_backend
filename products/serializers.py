from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Product
    fields = '__all__'

  def create(self, validated_data):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    return Product.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """
    Update and return an existing `Snippet` instance, given the validated data.
    """
    instance.name         = validated_data.get('name', instance.name)
    instance.price        = validated_data.get('price', instance.price)
    instance.description  = validated_data.get('description', instance.description)
    instance.is_active    = validated_data.get('is_active', instance.is_active)

    instance.path_img     = validated_data.get('path_img', instance.path_img)
    instance.url_img      = validated_data.get('url_img', instance.url_img)

    instance.save()
    return instance