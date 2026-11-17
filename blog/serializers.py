from .models import Blog
from rest_framework import serializers

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']