from datetime import datetime

from rest_framework import serializers

from football_app.country.serializers import CountrySerializer
from .models import League


class LeagueShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    country_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = League
        fields = ('id', 'name', 'season', 'logo', 'country_id',)


class LeagueFullSerializer(LeagueShortSerializer):
    country = CountrySerializer(read_only=True)
    seasonStart = serializers.DateTimeField(default=datetime.now())
    seasonEnd = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = League
        fields = LeagueShortSerializer.Meta.fields + ('country', 'seasonStart', 'seasonEnd',)
