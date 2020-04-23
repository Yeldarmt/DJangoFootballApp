from rest_framework import serializers
from football_app.team.serializers import TeamShortSerializer
from football_app.referee.serializers import RefereeSerializer
from football_app.game.models import Game
from football_app.team.models import Team
from itertools import chain
import logging

logger = logging.getLogger('game')


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
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
    stadium = serializers.CharField(required=True)
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

    def validate_stadium(self, value):
        if len(value) < 15:
            logger.debug(f'Stadium name must be more than 15 character')
            logger.info(f'Stadium name must be more than 15 character')
            logger.warning(f'Stadium name must be more than 15 character')
            logger.error(f'Stadium name must be more than 15 character')
            logger.critical(f'Stadium name must be more than 15 character')
            raise serializers.ValidationError('Very short stadium name')
        return value


class GameEndSerializer(serializers.ModelSerializer):
    first_team_id = serializers.IntegerField(write_only=True)
    second_team_id = serializers.IntegerField(write_only=True)
    isActiveGame = serializers.BooleanField(required=True)

    class Meta:
        model = Game
        fields = ('isActiveGame', 'first_team_id', 'second_team_id')

    def update(self, instance, validated_data):
        instance.isActiveGame = validated_data.get('isActiveGame', instance.isActiveGame)
        team_one = Team.objects.get(id=validated_data.get('first_team_id'))
        team_second = Team.objects.get(id=validated_data.get('second_team_id'))
        players = list(chain(team_one.players.all(), team_second.players.all()))
        for player in players:
            if not player.isReserved:
                player_stata = player.statistica
                player_stata.played_games = player_stata.played_games + 1
                player_stata.save()
                player.save()
                print('player : ', player)
        instance.save()
        return instance

    def validate_isActiveGame(self, value):
        if value:
            raise serializers.ValidationError('Please, send a false to end the game')
        return value
