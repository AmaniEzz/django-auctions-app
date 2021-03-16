# Django-Auctions-webiste

### view webiste here ---> [https://djangoauctionapp.herokuapp.com/](https://djangoauctionapp.herokuapp.com/)

```
An eBay-like e-commerce auction site that allow users to:
- post auction listings
- place bids on listings (with constrains)
- comment on those listings
- and add listings to a “watchlist”
- checking their win list (after auction is end, user will see the items they won in winlist)
- adding items to cart (cart is not yet complete)
- but NO CHECKOUT!
``` 
# API 

| Method                        | URL                   | Description
| ----------------------------- |:------------------- |:------------------------------------------------------------------------------------|
| `GET`, `POST`| `/api/lisitngs/` | API endpoint to view all listings or create a new listing,
| `GET`, `PATCH`, `PUT`, `DELETE`        | `/api/lisitngs/:listing_id` | API endpoint to retrieve, update, edit or delete a lisitng object with given listing_id.    All users can accsess the listing, but only listings's seller can modify or delete it. User should be logged in|
| `POST`| `listings/:listing_id/make_bid/` |  API endpoint that alow making a bid on a listing with given listing_id, and display it if created successfully, JSON --> { "bid_value": you_bid},  User should be logged in|
| `GET` | `/api/comments/` | API endpoint that allows all comments to be viewed. User should be logged in}
| `GET` | `/api/watchlists/` | API endpoint that lists all bids made by users, you can filter them by bid's id or it's listing_id|
| `GET` | `/api/bids/` |  API endpoint that lists all Watchlists , you can filter by listing id to see which user has this listing in their watchlist, or you can filter by the username of watchlists's owner|
| `GET` | `/api/categories/` |

---

# Technology stack

### Django 3.0.3
### Django REST Framwork
### Heroku deployment
### Heroku PostgreSQL add on


