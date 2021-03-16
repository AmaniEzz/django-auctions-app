from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class User(AbstractUser):
    pass


# Table of Categories
class Categories(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


# Table comments, stores all info related to a commnet
class Comment(models.Model):
    
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    listingid = models.CharField(max_length=100)
    comment   = models.CharField(max_length=500)
    date      = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.comment}"


# Table of all Listings in website
class Listings(models.Model):
    seller        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    title         = models.CharField(max_length=100)
    description   = models.TextField()
    starting_bid  = models.DecimalField(max_digits=10, decimal_places=2)
    highest_bid   = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desired_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category      = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="category", blank=True, null=True)
    image         = models.CharField(max_length=500)
    created_at    = models.DateTimeField(auto_now_add=True)
    Winner        = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="winner", null=True)
    active        = models.BooleanField(default=True)
    comment       = models.ManyToManyField(Comment, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('listingpage', args=[(self.pk)])
   

# Table bid, stores all info related to a bid
class Bid(models.Model):
    id          = models.AutoField(primary_key=True, serialize=False)
    bidder      = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_owner")
    listingid   = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="Bid_listing")
    bid_value   = models.DecimalField(max_digits=10, decimal_places=2)
    date        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"A bid of ({self.bid_value}$) made by ({self.bidder}) on an item named ( {self.listingid} )"


# Table to store the watchlist for each user
class Watchlist(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    listing   = models.ManyToManyField(Listings, blank=True, related_name="user_fav")

    def __str__(self):
       return f"{self.user}'s WatchList"
