from django.urls import path

from . import views

urlpatterns = [
    path("listings/", views.ListingsView),
    path("listings/<int:listing_id>/", views.listing),
    path("comments/", views.Comments),
    path("watchlists/", views.WatchListsView.as_view()),
    path("comments/<int:pk>/", views.single_comment),
    path("bids/", views.Bids),
    path("bids/<int:listing_id>", views.single_bid),
    path("categories/", views.CategoriesView.as_view()),

]