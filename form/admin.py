from django.contrib import admin
from form.models import form
from form.models import groomingform
from form.models import healthform

class formAdmin(admin.ModelAdmin):
    list_display=('name','email','phoneno','address','pettype','message')
admin.site.register(form,formAdmin)

class gformAdmin(admin.ModelAdmin):
    list_display=('name','email','phoneno','address','pettype','date','time')
admin.site.register(groomingform,gformAdmin)

class hformAdmin(admin.ModelAdmin):
    list_display=('name','email','phoneno','address','pettype','date','time','message')
admin.site.register(healthform,hformAdmin)
# Register your models here.
