from rest_framework import serializers
from auctions.models import User, Listings, Bid, Comment, Watchlist, Categories
import django_filters



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_superuser:
            representation['admin'] = True
        return representation


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class ListingsSerializer(serializers.ModelSerializer):
    seller = serializers.StringRelatedField(read_only=True)
    Winner = serializers.StringRelatedField()
    comment = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Listings
        fields = "__all__"



class BidsSerializer(serializers.ModelSerializer):
    bidder = serializers.StringRelatedField(read_only=True)
    listingid = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Bid
        fields = "__all__"
        

class WatchListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    count = serializers.IntegerField(source='get_count')
    listing = serializers.SerializerMethodField()

    class Meta:
        model = Watchlist
        fields = "__all__"

    def get_listing(self, obj):
        listings = obj.listing.all()
        if not listings:
            return None
        return ListingsSerializer(listings, many=True).data

