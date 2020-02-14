from rest_framework import serializers
from mysite.models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields=('name', 'comment', 'regi_date')