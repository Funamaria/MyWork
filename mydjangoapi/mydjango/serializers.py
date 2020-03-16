from rest_framework import serializers
from mydjango.models import Content, Goods

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields=('name', 'comment')

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields=('name','description','price','category','image','url')