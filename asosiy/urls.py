from django.urls import path
from .views import *

urlpatterns = [
    path('bolim/', BolimView.as_view(), name="bolim"),
    path('mahsulotlar/', MahsulotView.as_view(), name="mahsulotlar"),
    path('mahsulot_edit/<int:pk>/', MahsulotEdit.as_view(), name="mahsulot_edit"),
    path('client/', ClientView.as_view(), name="client"),
]


