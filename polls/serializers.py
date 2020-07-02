from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth.models import Group


class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializers(serializers.ModelSerializer):
    choices = ChoiceSerializers(many=True, read_only=True, required=False)
    
    class Meta:
        model = Poll
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password','groups')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validate_data):
        user = User(
            email=validate_data['email'],
            username=validate_data['username'],
        )
        user.set_password(validate_data['password'])
        user.save()
        user.groups.set(validate_data['groups'])
        user.save()
        Token.objects.create(user=user)
        return user
