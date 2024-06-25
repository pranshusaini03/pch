from django.contrib import admin
from adoption.models import dadopt
from adoption.models import kadopt
from adoption.models import ladopt
from adoption.models import madopt
from adoption.models import hadopt
from adoption.models import badopt

class dadoptAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(dadopt,dadoptAdmin)

class kadoptAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(kadopt,kadoptAdmin)

class ladoptAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(ladopt,ladoptAdmin)

class hadoptAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(hadopt,hadoptAdmin)

class madoptAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(madopt,madoptAdmin)

class badoptAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(badopt,badoptAdmin)
# Register your models here.
