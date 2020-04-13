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
        print('goaler : ', Player.objects.get(id=validated_data.get('goalPlayer_id')))
        print('assistPlayer : ', Player.objects.get(id=validated_data.get('assistPlayer_id')))
        return goal

    class Meta:
        model = Goal
        fields = ('id', 'game_id', 'goalPlayer_id', 'assistPlayer_id', 'recordTime')
