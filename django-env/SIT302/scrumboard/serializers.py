from rest_framework import serializers

from .models import List, Card
#  ModelSerializer autogenerates JSON based fields


class CardSerializer(serializers.ModelSerializer):  # These classes allow the user to see all of there cards

    class Meta:
        model = Card

        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):  # These classes allow the user to see all of there cards
    cards = CardSerializer(read_only=True, many=True)

    class Meta:  # Meta class allows, Not to sure atm
        model = List

        fields = '__all__'  # Fields fixes up a assertion error

