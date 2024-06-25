from django.contrib import admin
from product.models import products
class productAdmin(admin.ModelAdmin):
    list_display=('image','name','price','message','pet','type1')
admin.site.register(products,productAdmin)
# Register your models here.
# Register your models here.
