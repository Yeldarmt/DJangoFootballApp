from rest_framework import serializers
from football_app.referee.models import Referee


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ('id', 'name', 'surname', 'nationality', 'level', 'salary')
