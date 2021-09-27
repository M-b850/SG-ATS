from django.urls import path
from inform.views import index, InformCreateView

urlpatterns = [
    path('', index, name='index'),
    path('send-inform-email/', InformCreateView.as_view(), name='send-inform-email'),
]