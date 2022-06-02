from django.urls import path
from .views import MessageModelViewSet

app_name = 'messageapp'

urlpatterns = [
    path('', MessageModelViewSet.as_view({'get': 'list'})),
]