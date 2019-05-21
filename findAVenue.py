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
    """Get longitude and latitude for input string from Google geolocation API.
    """

    city = inputString.replace(" ", "+")

    # Want results back in a JSON.  Adding API key and input string to query."
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={google_api_key}"

    # Request url and make the response a json that Python can read.
    r = requests.get(url).json()

    latitude = r["results"][0]["geometry"]["location"]["lat"]
    longitude = r["results"][0]["geometry"]["location"]["lng"]

    return (latitude, longitude)


def findAVenue(location):
    """Find a venue on Forsquare."""

    latitude, longitude = getGeocodeLocation(location)
    # Dog-friendly places, according to Foursquare API Docs = 13.
    features = 13
    # Only return one match.
    matches = 1

    url = f"https://api.foursquare.com/v2/venues/search?=client_id={forsquare_client_id}&client_secret={forsquare_client_secret}&v=20190521&ll={latitude},{longitude}&features={features}&limit={matches}"""  

    r = requests.get(url).json()

    if r["response"]["venues"]:
        venue = {}
        venue_id = r["response"]["venues"][0]["id"]
        venue["name"] = r["response"]["venues"][0]["name"]
        venue_address = r["response"]["venues"][0]["location"]["formattedAddress"]

        # Format venue address in one string.
        address = ""

        for i in venue_address:
            address += i + " "

        venue["address"] = address

        # Get venue photo via another request.
        url = f"https://api.foursquare.com/v2/venues/{venue_id}/photos?client_id={forsquare_client_id}&v=20190521&client_secret={forsquare_client_secret}"""

        r = requests.get(url).json()

        if r["response"]["photos"]["items"]:
            firstpic = r["response"]["photos"]["items"][0]
            prefix = firstpic["prefix"]
            suffix = firstpic["suffix"]
            img_url = f"{prefix}300x300{suffix}"
        else:
            img_url = """https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2F
                         images%2F38670528%2F108919755319%2F1%2Foriginal.jpg?
                         auto=compress&s=32c728ebfab7bb7cab9cf42307962b37"""

        venue["img_url"] = img_url

        return venue
    else:

        return "No matching venues."


################################################################################
# Enable running at command line.

if __name__ == "__main__":
    # Assess function output.

    findAVenue("Tokyo, Japan")
    findAVenue("New York, NY")
    findAVenue("San Francisco, CA")
    findAVenue("Los Angeles, CA")


