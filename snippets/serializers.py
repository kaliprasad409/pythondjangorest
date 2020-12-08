from rest_framework import serializers
from django.contrib.auth.models import User, Group



from .models import Snippets


class SnippetsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style','owner']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippets.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
