from django.urls import path
from .views import *


urlpatterns = [
    path('', kraskaApi.as_view(), name="home"),
    path('g', ali, name="detaiaa"),
    path('generic/<int:id>/', GenericAPIView.as_view(), name="detail"),
    path('generic', GenericAPIView.as_view(), name="detail"),
    path('generic/<int:id>/', GenericAPIView.as_view(), name="detail")

]