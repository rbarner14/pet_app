# For jsonifying response from call.
import json 
# For API calls.
import requests
# For API Keys.
import os

# API Keys.
forsquare_client_id = os.environ.get("FORSQUARE_CLIENT_ID")
forsquare_client_secret = os.environ.get("FORSQUARE_CLIENT_SECRET")
google_api_key = os.environ.get("GOOGLE_API_KEY")

def getGeocodeLocation(inputString):
    """Get longitude and latitude for input string from Google geolocation 
    API.
    """
    city = inputString.replace(" ", "+")

    # Want results back in a JSON.  Adding API key and input string to query."
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={google_api_key}"

    # Request url and make the response a json that Python can read.
    r = requests.get(url).json()

    longitude = r["results"][0]["geometry"]

    return (longitude,latitude)



def findAVenue(location):
    """Find a venue on Forsquare."""

    getGeocodeLocation(location)