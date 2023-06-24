from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Post, Group, Comment


class CommentSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post',)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'pub_date',
            'author',
            'image',
            'group',
            'comments'
        )
