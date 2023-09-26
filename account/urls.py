
from django.urls import path
from .views import UserRagitrationView,UserLoginViews,UserLogoutViews,UserBankAccountUpdateView
urlpatterns = [
    path('register/',UserRagitrationView.as_view(), name='register'),
    path('login/',UserLoginViews.as_view(), name='login'),
    path('logout/',UserLogoutViews.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
    
]
