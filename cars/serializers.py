from rest_framework import serializers
from .models import Car, Make, Model as CarModel, BodyType, Feature


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id', 'name', 'country', 'logo']

class ModelSerializer(serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(queryset=Make.objects.all())

    class Meta:
        model = CarModel
        fields = ['id', 'make', 'name']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['make'] = MakeSerializer(instance.make).data
        return rep

class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ['id', 'name', 'image']

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'category']