from rest_framework import serializers


class UserSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	username = serializers.CharField()
	first_name = serializers.CharField()
	last_name = serializers.CharField()
	email = serializers.CharField()
	price = serializers.IntegerField()
	rating = serializers.IntegerField()

