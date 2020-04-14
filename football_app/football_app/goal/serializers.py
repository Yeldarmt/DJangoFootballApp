from rest_framework import serializers
from football_app.goal.models import Goal
from football_app.player.models import Player
from football_app.player.serializers import PlayerShortSerializer
from football_app.game.serializers import GameSerializer2


class GoalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    game_id = serializers.IntegerField()
    goalPlayer_id = serializers.IntegerField()
    assistPlayer_id = serializers.IntegerField()
    recordTime = serializers.IntegerField()

    def create(self, validated_data):
        goal = Goal(**validated_data)
        goal.save()
        goaler = Player.objects.get(id=validated_data.get('goalPlayer_id'))
        goaler_stata = goaler.statistica
        goaler_stata.goals = goaler_stata.goals + 1
        goaler_stata.save()
        goaler.save()
        assistent = Player.objects.get(id=validated_data.get('assistPlayer_id'))
        assistent_stata = assistent.statistica
        assistent_stata.assists = assistent_stata.assists + 1
        assistent_stata.save()
        assistent.save()
        return goal

    class Meta:
        model = Goal
        fields = ('id', 'game_id', 'goalPlayer_id', 'assistPlayer_id', 'recordTime')
