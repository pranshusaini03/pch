from django.contrib import admin
from login.models import login
class loginAdmin(admin.ModelAdmin):
    list_display=('name','email','password','confirm_password')
admin.site.register(login,loginAdmin)
# Register your models here.
