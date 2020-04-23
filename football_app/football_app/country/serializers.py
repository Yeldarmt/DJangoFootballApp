from rest_framework import serializers
from .models import Country

import logging
logger=logging.getLogger('validation')
class CountrySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'code','flag', )

    def validate_name(self,value):
        if value[0]<'A' or value[0]>'Z':
            logger.error(f'Country name validation error: {value}')
            raise serializers.ValidationError('The name of country should with upper case letter!!!')
        return value