from jinja2 import StrictUndefined
from flask import (Flask, redirect, render_template, request, session, jsonify,
                   flash)
from flash_debugtoolbar import DebugToolbarExtension
import requests
import os
import random
import time

# API keys.
forsquare_client_id = os.enviorn.get("FORSQUARE_CLIENT_ID")
forsquare_client_secret = os.enviorn.get("FORSQUARE_CLIENT_SECRET")
google_api_key = os.enviorn.get("GOOGLE_API_KEY")

