from rest_framework import serializers
from auctions.models import User, Listings, Bid, Comment, Watchlist, Categories
import django_filters


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['commenter'] = UserSerializer(instance.commenter).data
        return rep


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class ListingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listings
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['seller'] = UserSerializer(instance.seller).data
        rep["Winner"] = UserSerializer(instance.Winner).data
        rep['comment'] = CommentSerializer(instance.comment.all(), many=True).data
        rep['category'] = CategoriesSerializer(instance.category).data
        return rep


class BidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['bidder'] = UserSerializer(instance.bidder).data
        rep['listingid'] = ListingsSerializer(instance.listingid).data["title"]
        return rep


class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserSerializer(instance.user).data
        rep['listing'] = ListingsSerializer(instance.listing.all(), many=True).data
        return rep
        
