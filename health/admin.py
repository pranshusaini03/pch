from django.contrib import admin
from health.models import ddoctor
from health.models import kdoctor
from health.models import ldoctor
from health.models import mdoctor
from health.models import hdoctor
from health.models import bdoctor

class ddoctorAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(ddoctor,ddoctorAdmin)

class kdoctorAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(kdoctor,kdoctorAdmin)

class ldoctorAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(ldoctor,ldoctorAdmin)

class hdoctorAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(hdoctor,hdoctorAdmin)

class mdoctorAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(mdoctor,mdoctorAdmin)

class bdoctorAdmin(admin.ModelAdmin):
    list_display=('image','name','shortaddress','address','phone_no','opening_Hours','rating')
admin.site.register(bdoctor,bdoctorAdmin)
# Register your models here.
