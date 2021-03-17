from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import serializers, viewsets, routers
from rest_framework import permissions
from auctions.models import Listings, Bid, Comment, Watchlist, Categories
from .serializers import ListingsSerializer, CategoriesSerializer, CommentSerializer, BidsSerializer, WatchListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView

################################################### All GET methods ##############################################


class ListingsView(generics.ListCreateAPIView):
    """
    API endpoint that allows all Listings to be viewed or create a new listing.
    """

    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer

    # Filter listing by the it's id, active state or seller__username (eg. "/api/listing/?active=false")
    filter_fields = ['active', 'seller__username', 'id']
    filter_backends = [DjangoFilterBackend]


class ListingDetailsView(APIView):

    """
    API endpointa that retrieve, update, edit or delete a lisitng object with given id.
    """

    def get_object(self, listing_id):

        '''
        Helper method to get the object with given listing_id and given seller id
        '''
        try:
            return Listings.objects.get(pk=listing_id)
        except Listings.DoesNotExist:
            return None
    # 1. Retrieve
    def get(self, request, listing_id, *args, **kwargs):
        '''
        Retrieves the detail of the listing with given listing_id
        '''
        listing_instance =  self.get_object(listing_id)
        if not listing_instance:
            return Response(
                {"res": "Listing with the given id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        listings_serializer = ListingsSerializer(listing_instance)
        return Response(listings_serializer.data, status=status.HTTP_200_OK)

    # 2. Update
    def patch(self, request, listing_id, **kwargs):
        '''
        Updates the listing with given listing_id if exists,
        '''

        listing_instance = self.get_object(listing_id)
        if not listing_instance:
            return Response(
                {"res": "Listing with the given id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST)

        data = JSONParser().parse(request)
        listings_serializer = ListingsSerializer(instance = listing_instance, data=data, partial = True)
        if listings_serializer.is_valid():
            listings_serializer.save()
            return Response(listings_serializer.data, status=status.HTTP_200_OK)
        return Response(listings_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    # 3. edit
    def put(self, request, listing_id, *args, **kwargs):
        '''
        Updates the listing with given listing_id if exists
        '''
        listing_instance = self.get_object(listing_id)
        if not listing_instance:
            return Response(
                {"res": "Listing with the given id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'), 
            'description':  request.data.get('description'), 
            'starting_bid': request.data.get("starting_bid"),
            'desired_price': request.data.get("desired_price"),
            'image': request.data.get("image"),
            'active': request.data.get("active"),
        }

        listings_serializer = ListingsSerializer(instance = listing_instance, data=data, partial = True)
        if listings_serializer.is_valid():
            listings_serializer.save()
            return Response(listings_serializer.data, status=status.HTTP_200_OK)
        return Response(listings_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 4. Delete
    def delete(self, request, listing_id, *args, **kwargs):
        '''
        Deletes the listing item with given listing_id if exists
        '''
        listing_instance = self.get_object(listing_id)
        if not listing_instance:
            return Response(
                {"res": "Listing with the given id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        listing_instance.delete()
        return Response(
            {"res": "Listing deleted successfully!"},
            status=status.HTTP_200_OK
        )
   

class CommentsView(generics.ListAPIView):
    """
    API endpoint that allows all comments to be viewed.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # Filter comments by the it's "id" or "commenter" username (eg. "/api/comments/?commenter=Amany")
    filter_fields = ['id','commenter__username']
    filter_backends = [DjangoFilterBackend]


class ListBidsview(ListAPIView):

    """
    API endpoint that lists all bids made by users, you can filter them by bid's id or it's listing_id
    """

    queryset = Bid.objects.all()
    serializer_class = BidsSerializer
    filter_fields = ['id', 'listingid']
    filter_backends = [DjangoFilterBackend]


class WatchListsView(ListAPIView):

    """
    API endpoint that lists all Watchlists , you can filter by listing id to see which user has this listing in their watchlist, or you can filter by the username of watchlists's owner
    """
    queryset = Watchlist.objects.all()
    serializer_class = WatchListSerializer
    filter_fields = ['user__username', 'listing__id']
    filter_backends = [DjangoFilterBackend]
    

class CategoriesView(ListAPIView):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


@api_view(['GET','POST'])
def make_bid(request, listing_id):

    """
    API endpoint that alow making a bid on a listing with given listing_id, and display it if created successfully, JSON --> { "bid_value": you_bid}
    """
    # add permission to check if user is authenticated (logged in)
    permission_classes = [permissions.IsAuthenticated]
    item = Listings.objects.get(pk=listing_id)

    amount = request.data.get("bid_value")
    if amount is not None and amount <= item.desired_price and amount > item.highest_bid:
        data = {
                "bid_value": amount,
                "listingid": listing_id,
                "bidder": request.user.id,
                }

        serializer = BidsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            # Update the current price of the item, and the current winner
            item.highest_bid = amount
            item.Winner = request.user
            item.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Message": r"Please place a bid with value more than ${0}, and less than ${1}!" .format(item.highest_bid, item.desired_price)}, status=status.HTTP_200_OK)

