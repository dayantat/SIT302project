from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')  # this is the data we send back to the user

        # fields = '__all__'  # Fields fixes up a assertion error
