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

class CarSerializer(serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(queryset=Make.objects.all())
    model = serializers.PrimaryKeyRelatedField(queryset=CarModel.objects.all())
    body_type = serializers.PrimaryKeyRelatedField(queryset=BodyType.objects.all())
    features = serializers.PrimaryKeyRelatedField(queryset=Feature.objects.all(), many=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'body_type', 'fuel_type', 'transmission', 'color', 'mileage', 'engine_size', 'power', 'drive_type', 'features', 'vin', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['make'] = MakeSerializer(instance.make).data
        rep['model'] = ModelSerializer(instance.model).data
        rep['body_type'] = BodyTypeSerializer(instance.body_type).data
        rep['features'] = FeatureSerializer(instance.features.all(), many=True).data

        return rep