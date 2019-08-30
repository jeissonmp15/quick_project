from rest_framework.serializers import ModelSerializer

from city.models import City


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
