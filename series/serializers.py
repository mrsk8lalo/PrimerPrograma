from rest_framework import serializers
from .models import series

class seriesSerializer(serializers.ModelSerializer):

#Representacion de los atributos
    class Meta:
             model = series
             fields = ('id', 'name', 'release_date', 'rating', 'category')

    def create(self, validated_data):# funcion para crear
        """
        Create and return a new `series` instance, given the validated data.
        """
        return series.objects.create(**validated_data)

    def update(self, instance, validated_data):#Funcion para actualizar
        """
        Update and return an existing `series` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
