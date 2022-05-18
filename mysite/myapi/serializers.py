from rest_framework import serializers

from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'message', 'created at', 'updated at', 'created by')
        created_by = {'id', 'username', 'email'} 