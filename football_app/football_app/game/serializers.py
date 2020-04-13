from rest_framework import serializers
from football_app.team.serializers import TeamShortSerializer
from football_app.referee.serializers import RefereeSerializer
from football_app.game.models import Game


class GameSerializer(serializers.Serializer):
    game_date = serializers.DateTimeField()
    score_team_one = serializers.IntegerField(required=False)
    score_team_second = serializers.IntegerField(required=False)
    stadium = serializers.CharField()
    isActiveGame = serializers.BooleanField(required=False)
    first_team = TeamShortSerializer()
    second_team = TeamShortSerializer()
    referee = RefereeSerializer()

    def create(self, validated_data):
        game = Game(**validated_data)
        game.save()
        return game

    def update(self, instance, validated_data):
        instance.isActiveGame = validated_data.get('isActiveGame', instance.isActiveGame)
        instance.score_team_one = validated_data.get('score_team_one', instance.score_team_one)
        instance.score_team_second = validated_data.get('score_team_second', instance.score_team_second)
        instance.save()
        return instance


class GameSerializer2(serializers.Serializer):
    game_date = serializers.DateTimeField()
    score_team_one = serializers.IntegerField(required=False)
    score_team_second = serializers.IntegerField(required=False)
    stadium = serializers.CharField()
    isActiveGame = serializers.BooleanField()
    first_team_id = serializers.IntegerField(write_only=True)
    second_team_id = serializers.IntegerField(write_only=True)
    referee_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        game = Game(**validated_data)
        game.save()
        return game

    def update(self, instance, validated_data):
        instance.isActiveGame = validated_data.get('isActiveGame', instance.isActiveGame)
        instance.score_team_one = validated_data.get('score_team_one', instance.score_team_one)
        instance.score_team_second = validated_data.get('score_team_second', instance.score_team_second)
        instance.save()
        return instance
