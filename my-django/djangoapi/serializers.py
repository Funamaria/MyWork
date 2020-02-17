from rest_framework import serializers
from djangoapi.models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields=('name','comment')