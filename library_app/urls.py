from django.urls import path
from . import views
urlpatterns=[
    path('',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('home/',views.home,name='home'),
    path('books/',views.book_list,name='book_list'),
]