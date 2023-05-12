from django.urls import path
from .views import home,flightDetail,flightBooking,logout,\
    myBooking,myProfile,bookingHistory,flightList,\
    register,login,addPassenger,bookingConfirm

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('flightList/',flightList.as_view(),name='flightList'),
    path('flightDetail/',flightDetail.as_view(),name='flightDetail'),
    path('flightBooking/',flightBooking.as_view(),name='flightBooking'),
    path('myProfile/', myProfile.as_view(), name='myProfile'),
    path('myBooking/', myBooking.as_view(), name='myBooking'),
    path('bookingHistory/', bookingHistory.as_view(), name='bookingHistory'),
    path('logout/', logout.as_view(), name='logout'),
    path('login/', login.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('addPassenger/', addPassenger.as_view(), name='addPassenger'),
path('myProfile/flightList/',flightList.as_view(),name='flightList'),
path('addPassenger/flightList/',flightList.as_view(),name='flightList'),
path('myBooking/flightList/',flightList.as_view(),name='flightList'),
path('flightList/flightList/',flightList.as_view(),name='flightList'),
path('flightDetail/flightList/',flightList.as_view(),name='flightList'),
path('bookingHistory/flightList/',flightList.as_view(),name='flightList'),
]