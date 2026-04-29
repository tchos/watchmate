from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    # une wathlist possede plusieurs review
    # reviews provient de related_name dans models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # une plateforme possede plusieurs watchlist
    # watchlist provient de related_name dans platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many = True) # Va afficher ce que vous avez defini dans la fonction __str__ de chaque modele

    url = serializers.HyperlinkedIdentityField(
        view_name='watchlist:stream-detail'
    )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

"""
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
"""
"""
# validation des valeurs des champs: Methode 1
def name_length_validator(value):
    if len(value) < 3:
        raise serializers.ValidationError({'Error': 'Nom trop court !'})

class MovieSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(validators=[name_length_validator])
    # champ calculé
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        #fields = ('id', 'name', 'description', 'active') # quand certains chanps
        # exclude = ('active',) # quand veut tous les chanps sauf un champ particulier
        fields = "__all__"

    def get_len_name(self, obj):
            return len(obj.name)

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError({'name': 'Name and description cannot be same'})
        else:
            return data

    # validation des valeurs des champs: Methode 2
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'Error': 'Nom trop court !'})
        else:
            return value


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

    # validation des valeurs des champs: Methode 2
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'Error': 'Nom trop court !'})
        else:
            return value

"""