from rest_framework import serializers
from football_app.referee.models import Referee


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ('name', 'surname', )


class RefereeFullSerializer(RefereeSerializer):
    class Meta(RefereeSerializer.Meta):
        fields = RefereeSerializer.Meta.fields + ('id', 'nationality', 'level', 'salary')
