from rest_framework import serializers
from football_app.statistica.serializers import StatisticsSerializer
from football_app.team.serializers import TeamShortSerializer
from football_app.player.models import Player


class PlayerShortSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    position = serializers.CharField()
    number = serializers.IntegerField()
    team = TeamShortSerializer()

    def create(self, validated_data):
        player = Player(**validated_data)
        player.save()
        return player

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance


class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    nationality = serializers.CharField()
    age = serializers.IntegerField()
    date_of_birth = serializers.DateField()
    photo = serializers.ImageField(required=False)
    height = serializers.FloatField()
    weight = serializers.FloatField()
    position = serializers.CharField()
    number = serializers.IntegerField()
    salary = serializers.IntegerField()
    isReserved = serializers.BooleanField()
    team = TeamShortSerializer(read_only=True)
    team_id = serializers.IntegerField(write_only=True)
    statistica = StatisticsSerializer(read_only=True)
    statistica_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        player = Player(**validated_data)
        player.save()
        return player

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        instance.number = validated_data.get('number', instance.number)
        instance.team_id = validated_data.get('team_id', instance.team_id)
        instance.save()
        return instance
