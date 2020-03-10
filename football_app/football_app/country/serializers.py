from rest_framework import serializers
from .models import Country



class CountrySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'code','flag', )

    def validate_name(self,value):
        if value[0]<'A' or value[0]>'Z':
            raise serializers.ValidationError('The name of country should with upper case letter!!!')
        return value