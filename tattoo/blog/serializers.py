from rest_framework import serializers

from master.serializers import MasterListSerializer
from .models import Tag, Post, Comment


class TagSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода тегов"""
    class Meta:
        model = Tag
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода списка постов"""
    tags = TagSerializer(read_only=True, many=True)
    author = MasterListSerializer(read_only=True)
    image = serializers.ImageField(read_only=True)
    content = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода поста"""
    tags = TagSerializer(read_only=True, many=True)
    author = MasterListSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
