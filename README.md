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

| Method                        | URL                   | Action
| ----------------------------- |:------------------- |:------------------------------------------------------------------------------------|
| `GET`, `POST`| `/api/lisitngs/` | create or read a list of Listings
| `GET`, `PATCH`, `PUT`, `DELETE` | `/api/lisitngs/:listing_id` |  read, update, edit or delete a listing |
| `GET` | `/api/comments/` | create or read a list of comment |
| `GET` | `/api/watchlists/` | create or read a list of watchlists|
| `GET` | `/api/categories/` | create or read a list of categories

---

# Technology stack

### Django 3.0.3
### Django REST Framwork
### Heroku deployment
### Heroku PostgreSQL add on


