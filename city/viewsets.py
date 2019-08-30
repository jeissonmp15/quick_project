# Create your views here.
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from city.models import City
from city.serializers import CitySerializer
from city.tasks import proccess_file


class CityViewSet(ModelViewSet):
    model = City
    serializer_class = CitySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.model.objects.all()

    @action(methods=['post'], detail=False)
    def create_by_csv(self, request):
        if request.data.get('file') and request.FILES['file']:
            up_file = request.FILES['file']
            destination = open(up_file.name, 'wb+')
            for chunk in up_file.chunks():
                destination.write(chunk)
                destination.close()

            proccess_file(up_file.name)
            return Response()
        raise ValidationError('Por favor cargue un archivo')
