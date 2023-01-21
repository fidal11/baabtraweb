from django.urls import path
from . import views

urlpatterns = [
   path('home',views.b_home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('boot_strap',views.boot_strap,name='boot_strap'),

]
