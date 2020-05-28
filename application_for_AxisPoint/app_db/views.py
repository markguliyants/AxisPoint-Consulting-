from .models import GreetingsData
from .serializers import GreetingsDataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import BrowsableAPIRenderer
import django_filters.rest_framework
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


class DataViewSet(viewsets.ModelViewSet):  # группировка поведения в классы
    queryset = GreetingsData.objects.all()
    serializer_class = GreetingsDataSerializer
    filter_backends = [DjangoFilterBackend]  #
    filterset_fields = ['date']  # устанавливаем атрибут, указывая поля (фильтр по чему)
    renderer_classes = [JSONRenderer, XLSXRenderer, BrowsableAPIRenderer]

    @api_view(['GET'])
    def data(self, request):
        date = request.GET['date']
        if date:
            queryset = queryset.filter(GreetingsData__date=date)
        serializer = GreetingsDataSerializer(queryset, many=True)
        return Response(serializer.data)
