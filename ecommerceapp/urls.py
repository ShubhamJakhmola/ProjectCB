from django.urls import path
from ecommerceapp import views


urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('privacy',views.privacy,name="privacy"),
    path('profile',views.profile,name="profile"),
    path('checkout/', views.checkout, name="Checkout"),
    path('prodetail',views.prodetail,name="prodetail"),
    path('paytm/', views.paytm, name="paytm"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),

]
