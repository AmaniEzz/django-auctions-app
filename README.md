# Django Auctions site

```
An eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings,
comment on those listings, and add listings to a “watchlist.”
```

### see a live Demo video on [Youtube](https://www.youtube.com/watch?v=61lkNZD7zX4)
------------------------------------------------------------------------------------------

# Website Functionalities

- **PostgreSQL Database**: In this project, I've created 5 database tables, ***Listings*** table, ***Bid*** table, ***Comments*** table, ***Categories*** table and finally ***Categories*** table. In addition to Django abstract User model. Interactions with the database are done using Django ORM. see [Models.py](https://github.com/AmaniEzz/django-auctions-app/blob/master/auctions/models.py)

- **Create Listing page:** Logged in Users can visit a page to create a new listing. They're able to specify a title for the listing, a text-based description, a starting bid, the desired price, a URL for an image for the listing, and/or a category (e.g. Antique, Home, Electronics, Beauty, etc..).

- **Active Listings Page:** The default route of this web application lets users view all of the currently active auction listings. For each active listing, this page displays the title, description, current highest bid, and photo (if one exists for the listing).

- **Listing Page:** Clicking on a listing takes users to a page specific to that listing. On that page users
     - If the user is signed in, the user can add the item to their “Watchlist.” If the item is already on the watchlist, the user can remove it.
     - If the user is signed in, the user can place a bid on the item;
         - The bid must be at least as large as the starting bid (if no bid made yet), 
         - or must be greater than any other bids that have been placed. 
         - If a bid is greater than the desired price set by the seller, then the “Buy it now” option is removed (disabled), and the auction just continues.
         - If the bid doesn’t meet those criteria, the user is presented with an error.
     - If the user is signed in and is the one who created the listing (seller), he/she have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
     -  If the seller closed an auction that has no bids yet, they can reopen the auction again
     -  If a user is signed in on a closed listing page, and the user has won that auction, the page alters the user with a message saying so.

            
- **Commenting:**  Users who are signed in can add comments to the listing page. The listing page displays all comments that have been made on the listing.

- **Watchlist page:** Users who are signed in can visit a Watchlist page, which displays all of the listings that a user has added to their watchlist;
    -  Clicking on any of those listings should take the user to that listing’s page.
    -  User's watchlist only returns items that are active and not won by the user.
    -  If a user won a listing from their watchlist or if it's closed, then it'll be removed automatically from their watchlist.
    -  If a user tried to add an item to their watchlist and they already have it in their watchlist, alter message is displayed saying so.

 - **Winlist page:** If a signed-in user won an item, it's automatically placed on their winlist page, and removed from the watchlist (if exists).
    - User should add the items in their winlist to their shopping cart by clicking 'Add to cart, so that cart is updated with their bid price.
 
 - **Shopping cart:**: Users who are signed can add active items with the 'Buy it now' option enabled into their shopping cart, and remove it from the cart;
    - Shopping cart does not support Checkout at the moment.
       
 - **Categories page:** Users can visit a page that displays a list of all listing categories. Clicking on the name of any category takes the user to a page that displays all of the active listings in that category.

 - **Django Admin Interface:** Via the Django admin interface, a site administrator should can view, add, edit, and delete any listings, comments, watchlists, and bids made on the site.


-------------------------

# API 

| Method                        | URL                   | Action
| ----------------------------- |:------------------- |:------------------------------------------------------------------------------------|
| `GET`, `POST`| `/api/lisitngs/` | create or read a list of Listings
| `GET`, `PATCH`, `PUT`, `DELETE` | `/api/lisitngs/:listing_id` |  read, update, edit or delete a listing |
| `GET` | `/api/comments/` | create or read a list of comment |
| `GET` | `/api/watchlists/` | create or read a list of watchlists|
| `GET` | `/api/categories/` | create or read a list of categories


> See API's [views.py](https://github.com/AmaniEzz/django-auctions-app/blob/master/api/views.py)

-----

# Technology stack

### Django 3.0.3
### Django REST Framwork
### Heroku
### PostgreSQL
### HTML5/CSS
### Bootstrap 4
---
