from django.urls import path,include
from . import views

app_name = "carmaapp"

urlpatterns = [
    path('',views.home,name='home'),
    path('ride/<int:ride_id>/',views.ride_detail, name='ride_detail'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]
