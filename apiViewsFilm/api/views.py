from django.shortcuts import render
from .models import Film,Afish
from .serializers import Filmsterializer,Afishsterializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView


class FilmView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = Filmsterializer


class Film2View(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = Filmsterializer

class AfishView(ListAPIView):
    queryset = Afish.objects.all()
    serializer_class = Afishsterializer

class Afish2View(RetrieveUpdateDestroyAPIView):
    queryset = Afish.objects.all()
    serializer_class = Afishsterializer
