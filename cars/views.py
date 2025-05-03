from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .models import Car, Make, Model, Feature, BodyType
from .serializers import MakeSerializer, ModelSerializer, BodyTypeSerializer, FeatureSerializer, CarSerializer
from .pagination import MakePagination, ModelPagination, BodyTypePagination, FeaturePagination, CarPagination


class MakeListCreateView(generics.ListCreateAPIView):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer
    permission_classes = [AllowAny]
    pagination_class = MakePagination

class ModelListCreateView(generics.ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [AllowAny]
    pagination_class = ModelPagination

class ModelsByMake(generics.ListAPIView):
    serializer_class = ModelSerializer
    permission_classes = [AllowAny]
    pagination_class = ModelPagination

    def get_queryset(self):
        make_id = self.kwargs['make_id']
        return Model.objects.filter(make_id=make_id)

class BodyTypeListCreateView(generics.ListCreateAPIView):
    queryset = BodyType.objects.all()
    serializer_class = BodyTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = BodyTypePagination

class FeatureListCreateView(generics.ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [AllowAny]
    pagination_class = FeaturePagination

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = CarPagination