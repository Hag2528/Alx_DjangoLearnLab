
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email', 'password', 'bio', 'profile_picture', 'followers')
        extra_kwargs = {'password': {'write_only': True}}


        serializers.CharField() 
        Token.objects.create
        get_user_model().create_user