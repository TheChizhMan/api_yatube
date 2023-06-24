from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Преобразует информацию для работы через API по модели Post."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    comments = serializers.StringRelatedField(
        many=True,
        required=False
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Преобразует информацию для работы через API по модели Group."""

    class Meta:
        fields = '__all__'
        read_only_fields = ('title',)
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Преобразует информацию для работы через API по модели Comment."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',
                            'author',
                            'created')
        model = Comment
