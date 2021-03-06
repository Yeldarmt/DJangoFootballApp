from rest_framework import serializers
from football_app.statistica.models import Statistica


class StatisticsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    goals = serializers.IntegerField()
    assists = serializers.IntegerField()
    red_card = serializers.IntegerField()
    yellow_card = serializers.IntegerField()
    played_games = serializers.IntegerField()
    player_name = serializers.CharField(source='statistics.name', read_only=True)
    player_surname = serializers.CharField(source='statistics.surname', read_only=True)

    def create(self, validated_data):
        statistic = Statistica(**validated_data)
        statistic.save()
        return statistic

    def update(self, instance, validated_data):
        instance.goals = validated_data.get('goals', instance.goals)
        instance.assists = validated_data.get('assists', instance.assists)
        instance.red_card = instance.red_card + validated_data.get('red_card', instance.red_card)
        instance.yellow_card = instance.yellow_card + validated_data.get('yellow_card', instance.yellow_card)
        instance.played_games = validated_data.get('played_games', instance.played_games)
        instance.save()
        return instance

    def validate_red_card(self, value):
        if value > 1:
            raise serializers.ValidationError('Player can not get more than 1 red card on match')
        return value

    def validate_yellow_card(self, value):
        if value > 2:
            raise serializers.ValidationError('Player can not get more than 2 yellow card on match')
        return value
