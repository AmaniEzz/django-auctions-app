from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("listings/", views.ListingsView.as_view(), name='get_listings'),
    path("listings/create/", views.ListingsView.as_view(), name='create_listing'),

    path("listings/<int:listing_id>/", views.ListingDetailsView.as_view(), name="get_listing"),
    path("listings/<int:listing_id>/update/", views.ListingDetailsView.as_view(), name='update_listing'),
    path("listings/<int:listing_id>/edit/<str:field>", views.ListingDetailsView.as_view(), name='edit_listing'),
    path("listings/<int:listing_id>/delete/", views.ListingDetailsView.as_view(), name='delete_listing'),
    path("listings/<int:listing_id>/make_bid/", views.make_bid),

    path("comments/", views.CommentsView.as_view()),
    path("watchlists/", views.WatchListsView.as_view()),
    path("categories/", views.CategoriesView.as_view()),
    path("bids/", views.ListBidsview.as_view()),


]