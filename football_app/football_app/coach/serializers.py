from datetime import datetime, date

from rest_framework import serializers

from football_app.coach.models import Coach


class ListSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    surname=serializers.CharField(required=True)
    nationality=serializers.CharField(default="")
    age=serializers.IntegerField(default=0)
    height=serializers.IntegerField(default=0)
    weight=serializers.IntegerField(default=0)
    date_of_birth=serializers.DateField(default=date.today())
    salary=serializers.IntegerField(default=0)

    def create(self,validated_data):
        li=Coach(**validated_data)
        li.save()
        return li

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.save()
        return instance