##Patnox 27-07-2021

from rest_framework_json_api import serializers
from checkpoints.models import CheckedPoints

class CheckedPointsSerializer(serializers.HyperlinkedModelSerializer):
    response = serializers.ReadOnlyField()
    check_date = serializers.ReadOnlyField()
    class Meta:
        model = CheckedPoints
        fields = ('query', 'response', 'check_date')

