from django.urls import path
from . import views

urlpatterns = [
    path('film/', views.FilmView.as_view()),
    path('film/<str:pk>/', views.Film2View.as_view()),
    path('afish/',views.AfishView.as_view()),
    path('afish/<str:pk>/',views.Afish2View.as_view()),
]