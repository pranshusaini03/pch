from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static  # Import static function from django.conf.urls.static
from petcarehub import views
urlpatterns = [
path('', views.home),  
    path('admin/', admin.site.urls),
    path('save_cart/', views.save_cart, name='save_cart'),
    path('save_cart1/', views.save_cart1, name='save_cart1'),
    path('adoption/',views.adoption),
    path('health/',views.health),
    path('cart/',views.cart1),
    path('index/',views.index),
    path('save_form/',views.save_form, name='save_form'),
    path('grooming/',views.grooming),
    path('dgroomer/',views.dgrooming),
    path('kgroomer/',views.kgrooming),
    path('lgroomer/',views.lgrooming),
    path('mgroomer/',views.mgrooming),
    path('hgroomer/',views.hgrooming),
    path('bgroomer/',views.bgrooming),
    path('dhealth/',views.dhealths),
    path('khealth/',views.khealths),
    path('lhealth/',views.lhealths),
    path('mhealth/',views.mhealths),
    path('hhealth/',views.hhealths),
    path('bhealth/',views.bhealths),
    path('dadoption/',views.dadoption),
    path('kadoption/',views.kadoption),
    path('ladoption/',views.ladoption),
    path('madoption/',views.madoption),
    path('hadoption/',views.hadoption),
    path('badoption/',views.badoption),
    path('ps/',views.ps),
    path('form/',views.vform),
    path('gform/',views.gform),
    path('hform/',views.hform),
    path('save_gform/',views.save_gform,name='save_gform'),
    path('save_hform/',views.save_hform,name='save_hform'),
    path('signup/',views.signup),
    path('signin/',views.signin1),
    path('signout/',views.signout),]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
