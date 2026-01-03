from django.test import TestCase

# Create your tests here.



#forward geocoding 
#import requests

#address = "Ranchi, Jharkhand, India"
#url = "https://nominatim.openstreetmap.org/search"
#params = {"q": address, "format": "json", "limit": 1}

#response = requests.get(url, params=params, headers={"User-Agent": "YourApp"})
#data = response.json()

#if data:
 #   print("Latitude:", data[0]["lat"])
 #   print("Longitude:", data[0]["lon"])


 #revarse geocoding

# lat, lon = 23.3441, 85.3096
#url = "https://nominatim.openstreetmap.org/reverse"
#params = {"lat": lat, "lon": lon, "format": "json"}

#response = requests.get(url, params=params, headers={"User-Agent": "YourApp"})
#print(response.json()["display_name"])