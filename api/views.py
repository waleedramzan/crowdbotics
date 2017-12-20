from hello.models import Animal
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.serializers import APISerializer


class APIList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = APISerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class APIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = APISerializer

    def get_queryset(self):
        return Animal.objects.all().filter(user=self.request.user)