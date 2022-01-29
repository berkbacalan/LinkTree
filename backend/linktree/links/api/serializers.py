from asyncore import read
from pickletools import read_long1
from rest_framework import serializers
from links.models import Links


class LinkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    url = serializers.URLField()

    def create(self, validated_data):
        print(validated_data)
        return Links.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return instance
