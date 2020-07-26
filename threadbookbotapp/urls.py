from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('<int:card_id>', views.card, name='book'),
]