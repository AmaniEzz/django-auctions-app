from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("active_listing", views.active_listing, name="active_listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listingpage, name="listingpage"),
    path("Watchlist", views.watchlist_page, name="watchlist_page"),
    path("Winlist", views.Winlist, name="Winlist"),
    path("Watchlist/<int:product_id>", views.add_to_wishlist, name="add_to_wishlist"),
    path("create_listing", views.CreateListing.as_view(), name="create_listing"),
    path("all_categories", views.all_categories, name="all_categories"),
    path("category_active_list/<str:name>", views.category_active_list, name="category_active_list"),
    path("make_bid/<int:listing_id>", views.make_bid, name="make_bid"),
    path("view_winner/<int:listing_id>", views.view_winner, name="view_winner"),
    path("close/<int:listing_id>", views.close_auction, name="close_auction"),
    path("reopen_auction/<int:listing_id>", views.reopen_auction, name="reopen_auction"),
    path("add_comment/<int:listing_id>", views.add_comment, name="add_comment"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/',views.cart_detail,name='cart_detail'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 