from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Room, Owner, Event
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')

class EventSerializer(serializers.ModelSerializer):
    #client = UserSerializer(many=True, blank=True)

    class Meta:
        model = Event
        fields = ('id', 'room', 'title', 'owner', 'client', 'start', 'end', 'image')



class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('__all__')