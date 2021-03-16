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
### Method `GET`

| Method                  | URL
| ------------------------- |:------------------- |
| `GET` and `POST`| `/api/lisitngs/` |
| `GET`, `PATCH`, `PUT`, `DELETE` | `/api/lisitngs/:listing_id` |
| `POST`| `listings/:listing_id/make_bid/` |
| `GET` | `/api/comments/` |
| `GET` | `/api/watchlists/` |
| `GET` | `/api/bids/` |
| `GET` | `/api/categories/` |

---

# Technology stack

### Django 3.0.3
### Django REST Framwork
### Heroku deployment
### Heroku PostgreSQL add on


