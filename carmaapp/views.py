from django.shortcuts import render, get_object_or_404
from .models import Ride, UserProfile, User
from django.http import Http404

# Create your views here.
def home(request):
    latest_rides = Ride.objects.all()[:10]
    return render(request,'home.html',{'latest_rides':latest_rides})

def ride_detail(request,ride_id):
    ride = get_object_or_404(Ride, pk = ride_id)
    return render(request,'ride_detail.html',{'ride':ride})

def user_profile(request, username):
    # Retrieve the ride where the driver's username matches the provided username
    ride = get_object_or_404(Ride, driver__username=username)
    # Retrieve the driver's profile based on the car field of the ride
    profile = get_object_or_404(UserProfile, name=ride.driver)
    return render(request, 'user_profile.html', {'profile': profile})


