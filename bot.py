import tweepy
import requests
import random
import urllib.request
import time
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")

access_token = os.environ.get("access_token")
token_secret = os.environ.get("token_secret")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)

api = tweepy.API(auth)


para = [
    {
       "breed_id": "sphy" 
    },
    {
        "breed_id": "orie"
    }
]

response = requests.get("https://api.thecatapi.com/v1/images/search", params = random.choice(para))
img_url = response.json()[0]['url']
filename = img_url.split("/")[-1]

def tweet(url, message):
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        
        api.update_with_media(filename, status=message)
        os.remove(filename) 
    else:
        print("unable to download image")

tweet(img_url, "kitten pic!")
