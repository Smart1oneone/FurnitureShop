from django.contrib import admin

from orders.admin import OrderTabularAdmin
from users.models import User
from carts.admin import CartTabAdmin
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
   list_display = ["username", 'first_name',"last_name", "email", ]

   inlines = [CartTabAdmin,OrderTabularAdmin]




