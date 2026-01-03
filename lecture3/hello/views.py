#login here
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.shortcuts import render, get_object_or_404
from .models import Destination
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'hello/index.html')  # this is your "Home" page
def destinations(request):
    return render(request, 'hello/destinations.html')
def planYourTrip(request):
    return render(request, 'hello/planYourTrip.html')
def culture(request):
    return render(request, 'hello/culture.html')
def adventure(request):
    return render(request, 'hello/adventure.html')
def festivals(request):
    return render(request, 'hello/festivals.html')
def contact(request):
    return render(request, 'hello/contact.html')
def history(request):
    return render(request, 'hello/history.html')
def localCuisine(request):
    return render(request, 'hello/localCuisine.html')
def test(request):
    return render(request, 'hello/test.html')
def login(request):
    return render(request, 'hello/login.html')
def map(request):
    return render(request, 'hello/map.html')
def login_view(request):
    return render(request, 'login_view.html')
def destination_detail(request, slug):
    place = get_object_or_404(Destination, slug=slug)
    return render(request, 'hello/destination_detail.html', {'place': place})


# 🔹 Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        print("👉 authenticate returned:", user)

        if user is not None:
            login(request, user)   # ✅ create session
            return redirect("dashboard")  # ✅ go to dashboard
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "hello/login.html")  # 👈 template path

# 🔹 Logout View
def logout_view(request):
    logout(request)  # ✅ destroy session
    return redirect("login")

# 🔹 Dashboard View
@login_required(login_url="login")
def dashboard(request):
    return render(request, "hello/dashboard.html", {"user": request.user})