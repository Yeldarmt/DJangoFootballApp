from rest_framework import serializers
from football_app.goal.models import Goal
from football_app.player.models import Player
from football_app.player.serializers import PlayerShortSerializer
from football_app.game.serializers import GameSerializer2


class GoalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    game_id = serializers.IntegerField()
    goalPlayer_id = serializers.IntegerField(write_only=True)
    goalPlayer = PlayerShortSerializer(read_only=True)
    assistPlayer_id = serializers.IntegerField(write_only=True)
    assistPlayer = PlayerShortSerializer(read_only=True)
    recordTime = serializers.IntegerField()

    def create(self, validated_data):
        goal = Goal(**validated_data)
        goal.save()
        goaler = Player.objects.get(id=validated_data.get('goalPlayer_id'))
        goal.add_goaler_goal(goaler)
        assistent = Player.objects.get(id=validated_data.get('assistPlayer_id'))
        goal.add_assist(assistent)
        return goal

    class Meta:
        model = Goal
        fields = ('id', 'game_id', 'goalPlayer_id', 'goalPlayer', 'assistPlayer_id', 'assistPlayer', 'recordTime')

    def validate(self, attrs):
        return attrs
