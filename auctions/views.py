from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Bid,Categories,Listings,Categories, Watchlist, Comment
from .models import User
from .forms  import ListForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.messages import add_message, ERROR,SUCCESS
from cart.cart import Cart


#############################################################################################################

def index(request):
    context = {"Listings": Listings.objects.all(),
               "user": request.user,
               "header": "Home"}
    return render(request, "auctions/index.html", context = context )   

def active_listing(request):
    context = {"Listings": Listings.objects.filter(active=True),
               "user": request.user,
               "header": "Active listings"}
    return render(request, "auctions/index.html", context = context )

#############################################################################################################

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

@login_required     
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


#############################################################################################################
def listingpage(request, listing_id):
    # retrive all comment under this listing
    context = {"listing": Listings.objects.get(pk=listing_id),
               "user": request.user, 
               "bids": Bid.objects.filter(listingid=listing_id),
               "comment_list": (Listings.objects.get(pk=listing_id).comment).all()}
    return render(request, "auctions/listing.html", context = context )   

class CreateListing(LoginRequiredMixin, CreateView):
    model = Listings
    form_class = ListForm

    def form_valid(self, form):
        form.instance.seller = self.request.user
        form.save()
        return super(CreateListing, self).form_valid(form)


#############################################################################################################
def all_categories(request):
    categories = Categories.objects.all()
    return render(request, "auctions/categories.html", context= {"categories" :categories})

def category_active_list(request, name):
    cat_type    = Categories.objects.get(category_name=name)
    cat_listing = Listings.objects.filter(category=cat_type, active=True)
    if cat_listing:
        return render(request, "auctions/index.html", context= {"Listings" :cat_listing } )
    else:
        return render(request, "auctions/errors.html", {"message": "Sorry, This Category has no active listings at the moment!"}) 

#############################################################################################################
@login_required     
def make_bid(request, listing_id, method=(["POST"])):
    amount = request.POST["amount"]
    item = Listings.objects.get(pk=listing_id)

    if amount is not None:
        # Save a new bid information in the Bid table
        new_bid = Bid(bidder=request.user, listingid=item, bid_value=amount)
        new_bid.save()

        # Update the current price of the item, and the current winner
        item.highest_bid = amount
        item.Winner = request.user
        item.save()
        
    return HttpResponseRedirect(reverse('listingpage', args=[listing_id]))


@login_required 
def view_winner(request, listing_id):
    pass

@login_required
def close_auction(request, listing_id):
    item = Listings.objects.get(pk=listing_id)
    item.active = False
    item.save()
    return HttpResponseRedirect(reverse('listingpage', args=[listing_id]))

     
@login_required
def reopen_auction(request, listing_id):
    item = Listings.objects.get(pk=listing_id)
    item.active=True
    item.save()
    return HttpResponseRedirect(reverse('listingpage', args=[listing_id]))


#############################################################################################################

@login_required
def watchlist_page(request):
    context = {"object_list": Watchlist.objects.filter(user=request.user)}
    return render(request, "auctions/watchlist_list.html", context = context )   

@login_required
def add_to_wishlist(request, product_id):
    item_to_save = Listings.objects.get(pk=product_id)

    # Check if the item already exists in that user watchlist
    if Watchlist.objects.filter(user=request.user, listing=product_id).exists():
        add_message(request, ERROR, "You already have it in your watchlist.")
        return HttpResponseRedirect(reverse("watchlist_page"))

    # Add the item through the ManyToManyField (Watchlist => item)
    else:
        user_list, created = Watchlist.objects.get_or_create(user=request.user)
        user_list.listing.add(item_to_save)
        #print((Watchlist.objects.get(user=request.user).listing).all())
        add_message(request, SUCCESS, "Successfully added to your watchlist")
        return HttpResponseRedirect(reverse("watchlist_page"))


#############################################################################################################
@login_required
def add_comment(request, listing_id):
    getListing = Listings.objects.get(pk=listing_id)
    comment = request.POST["comment"]
    new_comment = getListing.comment.create(comment=comment, listingid=getListing, commenter=request.user)
    return HttpResponseRedirect(reverse('listingpage', args=[listing_id]))

#############################################################################################################
############################################# Add to cart views ############################################

@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Listings.objects.get(pk=id)
    cart.add(product=product)
    return redirect("index")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Listings.objects.get(pk=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Listings.objects.get(pk=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Listings.objects.get(pk=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    context = {"listing": Listings.objects.all(),
    }
    return render(request, 'auctions/cart_detail.html', context=context)