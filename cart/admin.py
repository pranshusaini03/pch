from django.contrib import admin
from cart.models import cart
class cartAdmin(admin.ModelAdmin):
    list_display=('image','name','price','message')
admin.site.register(cart,cartAdmin)
# Register your models here.
