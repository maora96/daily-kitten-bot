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

headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'fd495732-c452-43e2-89fa-047521c950ef'
}

para = [
    {
       "breed_id": "sphy" 
    },
    {
        "breed_id": "orie"
    }
]


def tweet(message):
    interval = 60 * 2
    
    while True:
        response = requests.get("https://api.thecatapi.com/v1/images/search", params = random.choice(para), headers=headers)
        img_url = response.json()[0]['url']
        filename = img_url.split("/")[-1]
        request = requests.get(img_url, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)
            
            api.update_with_media(filename, status=message)
            os.remove(filename) 
            time.sleep(interval)
        else:
            print("unable to download image")

tweet("kitten pic! <3")
