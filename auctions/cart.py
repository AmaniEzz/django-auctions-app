from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, winner, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        id = product.pk
        newItem = True
        if product.active:
               self.cart[product.pk] = {
                  'userid': self.request.user.pk,
                  'product_id': id,
                  'name': product.title,
                  'price': str(product.desired_price),
                  'image': product.image
            }
        else:
            if(self.request.user.pk == winner.pk):
                  self.cart[product.pk] = {
                  'userid': self.request.user.pk,
                  'product_id': id,
                  'name': product.title,
                  'price': str(product.highest_bid),
                  'image': product.image }
            else:
                  self.cart[product.pk] = {
                  'userid': self.request.user.pk,
                  'product_id': id,
                  'name': product.title,
                  'price': str(product.desired_price),
                  'image': product.image
            }

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.pk)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
