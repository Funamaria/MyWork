from rest_framework import serializers
from mydjango.models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields=('name', 'comment')