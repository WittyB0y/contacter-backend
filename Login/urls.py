from django.urls import path

from .views import ObtainTokenView

urlpatterns = [
    path('login/', ObtainTokenView.as_view(), name='token'),
]
