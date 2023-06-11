# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from .views import UserViewSet
from .views import *

router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('user/<int:pk>/', UserScoreAPIView.as_view(), name='get_score'),
    path('', include(router.urls)),
]
