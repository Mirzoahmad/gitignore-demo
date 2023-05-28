from django.urls import path
from .views import view_cards,fake_api

app_name = 'cards'

urlpatterns = [
    path("", view_cards, name='view_cards'),
    path("<int:pk>/",view_cards, name='view_cards'),
    path('api/', fake_api, name='api'),
]