from rest_framework import serializers

from watchlist_app.models import Movie

# validation des valeurs des champs: Methode 1
def name_length_validator(value):
    if len(value) < 3:
        raise serializers.ValidationError({'Error': 'Nom trop court !'})

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length_validator])
    description = serializers.CharField()
    active = serializers.BooleanField()

    # pour la methode POST de def movies_list dans le fichier views
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    # validation des valeurs des champs: Methode 2
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError({'name':'Name and description cannot be same'})
        else:
            return data

    """# validation des valeurs des champs: Methode 2
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'Error': 'Nom trop court !'})
        else:
            return value
    """