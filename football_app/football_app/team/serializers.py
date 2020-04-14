from rest_framework import serializers

from football_app.country.serializers import CountrySerializer
from football_app.league.serializers import LeagueShortSerializer
from .models import League, Team

import logging
logger=logging.getLogger('validation')

class TeamShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    #league=LeagueSerializer(read_only=True)
    league_id=serializers.IntegerField(write_only=True)
    #country=CountrySerializer(read_only=True)
    country_id=serializers.IntegerField(write_only=True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'position','logo','wins','draws','losts','point',
                  'lasts_5','coach','goal_difference', 'short_code','league_id','country_id', )

    def validate_position(self, attrs):
        if (attrs<0):
            #logger.error(f'Teams position validation error: {attrs}')
            raise serializers.ValidationError('position field can not be negative')
        return attrs

    def validate_name(self, attrs):
        if (attrs[0]<'A' or attrs[0]>'Z'):
            logger.error(f'Teams name validation error: {attrs}')
            raise serializers.ValidationError('The name of Team should start with Upper case!!!')
        return attrs

    def validate_lasts_5(self, attrs):
        if len(attrs)!=5:
            logger.error(f'Teams last_5 value error: {attrs}')
            raise serializers.ValidationError('The length of lasts_5 field should be 5')
        return attrs

class TeamFullSerializer(TeamShortSerializer):
    league=LeagueShortSerializer(read_only=True)
    country=CountrySerializer(read_only=True)
    class Meta:
        model = Team
        fields = TeamShortSerializer.Meta.fields+('league','country',)

