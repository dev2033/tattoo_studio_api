from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet, ModelViewSet


from .models import Tag, Post, Comment
from .serializers import TagSerializer, PostListSerializer, PostDetailSerializer


class TagViewSet(ViewSet):
    """Вывод тегов"""
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Tag.objects.all()
        tag = get_object_or_404(queryset, pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)


class PostViewSet(ViewSet):
    """Вывод постов"""
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug: str):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)



