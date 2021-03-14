from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from auctions.models import Listings, Bid, Comment, Watchlist, Categories
from .serializers import ListingsSerializer, CategoriesSerializer, CommentSerializer, BidsSerializer, WatchListSerializer, WatchlistFilter


################################################### All GET methods ##############################################

@api_view(['GET', 'POST', 'DELETE'])
def ListingsView(request):
    if request.method == "GET": 
        listing  = Listings.objects.all()
        listing_serializer = ListingsSerializer(listing, many=True)

        content = {
        "listing": listing_serializer.data,
        }
        return Response(content)

    elif  request.method == "POST":
       pass

    elif  request.method == "DELETE":
        count = Listings.objects.all().delete()
        return Response({'message': '{} All listings were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
    


@api_view(['GET', 'POST', 'DELETE'])
def listing(request, listing_id):
    
    listing  = Listings.objects.filter(pk=listing_id)
    listing_serializer = ListingsSerializer(listing, many=True)

    content = {
        "listing": listing_serializer.data,
    }

    return Response(content)


@api_view(["GET"])
def Comments(request):
    
    comments  = Comment.objects.all()
    comments_serializer = CommentSerializer(comments, many=True)
    content = {
        "comments_list": comments_serializer.data,
    }

    return Response(content)



@api_view(["GET"])
def single_comment(request, pk):
    
    single_comment  = Comment.objects.filter(pk=pk)
    comment_serializer = CommentSerializer(single_comment, many=True)
    content = {
        "comment_details": comment_serializer.data,
    }

    return Response(content)



@api_view(["GET"])
def Bids(request):
    
    bids  = Bid.objects.all()
    bids_serializer = BidsSerializer(bids, many=True)
    content = {
        "Al_Bids": bids_serializer.data,
    }

    return Response(content)


@api_view(["GET"])
def single_bid(request, listing_id):
    
    single_bid  = Bid.objects.filter(pk=listing_id)
    bid_serializer = BidsSerializer(single_bid, many=True)
    content = {
        "bid_details": bid_serializer.data,
    }

    return Response(content)


class WatchListsView(ListAPIView):

    queryset = Watchlist.objects.all()
    serializer_class = WatchListSerializer
    filter_fields = ('user', 'listing')
    filter_class = WatchlistFilter


class CategoriesView(ListAPIView):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer



################################################### All Post methods ##############################################


