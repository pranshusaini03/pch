from django.contrib import admin
from grooming.models import dgroomer
from grooming.models import kgroomer
from grooming.models import lgroomer
from grooming.models import mgroomer
from grooming.models import hgroomer
from grooming.models import bgroomer

class dgroomerAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours')
admin.site.register(dgroomer,dgroomerAdmin)

class kgroomerAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours')
admin.site.register(kgroomer,kgroomerAdmin)

class lgroomerAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours')
admin.site.register(lgroomer,lgroomerAdmin)

class hgroomerAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours')
admin.site.register(hgroomer,hgroomerAdmin)

class mgroomerAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours')
admin.site.register(mgroomer,mgroomerAdmin)

class bgroomerAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours')
admin.site.register(bgroomer,bgroomerAdmin)
# Register your models here.
