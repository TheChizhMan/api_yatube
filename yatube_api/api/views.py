from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Объединяет логику для набора связанных представлений модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Создает публикацию с задаными полями."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Объединяет логику для набора связанных представлений модели Group.

    Представления работают только с безопасными запросами.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Объединяет логику для набора связанных представлений модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAuthorOrReadOnly, ]
    serializer_class = CommentSerializer

    def get_post(self):
        """Возвращает объект текущей записи."""
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Формирует queryset из комменатрия pk поста."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создает комментарий с задаными полями."""
        serializer.save(author=self.request.user, post=self.get_post())
