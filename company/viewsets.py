# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from company.models import Company
from company.serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    model = Company
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.model.objects.select_related('city')
