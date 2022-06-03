from django.shortcuts import render

# My Imports
from django.contrib.auth.decorators import login_required
# Function to render the frontend page
def frontend(request):
    return render(request,"frontend.html")
#-----------------------------BACKEND SECTION-----------------------|

# Function to render the backend page
@login_required(login_url="login")
def backend(request):
    return render(request,"backend.html")
