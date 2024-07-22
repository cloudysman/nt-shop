from django.urls import path
from .views import home_view, login_view, shop_view, signup_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('shop/', shop_view, name='shop'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
