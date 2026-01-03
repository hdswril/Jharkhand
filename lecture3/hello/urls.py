from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),  # this is your index.html
    path('destinations/', views.destinations, name='destinations'),
    path('planYourTrip/', views.planYourTrip, name='planYourTrip'),
    # ... more paths
    path('culture/', views.culture, name='culture'),
    path('adventure/', views.adventure, name='adventure'),
    path('festivals/', views.festivals, name='festivals'),
    path('contact/', views.contact, name='contact'),
    path('history/', views.history, name='history'),
    path('login/', views.login, name='login'),
    path('localCuisine/', views.localCuisine, name='localCuisine'),
    path('map/', views.map, name='map'),
    path('destination/<slug:slug>/', views.destination_detail, name='destination_detail'),
    ##path('login_view/', views.login_view, name='login_view'),


    #login 
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]