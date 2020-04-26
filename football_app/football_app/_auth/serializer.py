import datetime

from django.utils import timezone
from rest_framework import serializers

from football_app.game.serializers import GameSerializer
from football_app.team.serializers import TeamShortSerializer
from .models import MyUser, Notification
import logging
logger=logging.getLogger('validation')

class UserShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    favouriteTeam_id = serializers.IntegerField(write_only=True)
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name', 'address', 'favouriteTeam_id', 'birth_date', 'password',
                  'is_staff',)

    def validate_favouriteTeam_id(self, val):
        if val<0:
            logger.error(f'User favourite team validation is not correct: {val}')
            raise serializers.ValidationError('The foreign key id can not be negative!!!')
        return val

    def validate_first_name(self,value):
        if value[0]<'A' or value[0]>'Z':
            raise serializers.ValidationError('The name should with upper case letter!!!')
        return value

    def validate_last_name(self,value):
        if value[0]<'A' or value[0]>'Z':
            logger.error(f'User lastName validation is not correct: {value}')
            raise serializers.ValidationError('The lastname should with upper case letter!!!')
        return value



    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'],
                                          first_name=validated_data.get('first_name',''),
                                          last_name=validated_data.get('last_name',''),
                                          address=validated_data.get('address',''),
                                          favouriteTeam_id=validated_data.get('favouriteTeam_id',0),
                                          birth_date=validated_data.get('birth_date', "1999-07-04"))
        print(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user







class UserFullSerializer(UserShortSerializer):
    favouriteTeam = TeamShortSerializer(write_only=True)

    class Meta:
        model = MyUser
        fields = UserShortSerializer.Meta.fields + ('favouriteTeam',)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('is_staff',)


class NotificationSerializer(serializers.ModelSerializer):

    game=GameSerializer()
    class Meta:
        model=Notification
        fields=('game',)
