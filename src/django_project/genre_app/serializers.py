from rest_framework import serializers


class GenreOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField()
    categories = serializers.ListField(child=serializers.UUIDField())


class ListGenreOutputSerializer(serializers.Serializer):
    data = GenreOutputSerializer(many=True)
