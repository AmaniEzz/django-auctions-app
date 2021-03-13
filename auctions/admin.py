from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Comment)
admin.site.register(Listings)
admin.site.register(Bid)
admin.site.register(Watchlist)

