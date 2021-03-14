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
| `GET` | `/api/lisitngs/` |
| `GET` | `/api/lisitngs/:listing_id` |
| `GET` | `/api/comments/` |
| `GET` | `/api/lisitngs/:pk>` |
| `GET` | `/api/watchlists/` |
| `GET` | `/api/bids/` |
| `GET` | `/api/bids/:listing_id>` |
| `GET` | `/api/categories/` |

---

# Technology stack

### Django 3.0.3
### Django REST Framwork
### Heroku deployment
### Heroku PostgreSQL addon


