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

def dl_jpg(url, file_name):
    full_path = file_name
    urllib.request.urlretrieve(url, full_path)

req = urllib.request.build_opener()
req.addheaders = [{'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}]
urllib.request.install_opener(req)


dl_jpg(img_url, filename)

def tweet_image():
    interval = 60 * 5
    
    

    while True:
        print('tweeting kitty pic')
        api.update_with_media(filename, "here's a kitten <3")
        time.sleep(interval)


tweet_image()
