from django.urls import path, include
from .views import DataViewSet
from rest_framework import routers


# автоматически генерируем URL - адрес API
router = routers.SimpleRouter()
router.register(r'data', DataViewSet, basename='GreetingsData')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
