import tweepy
import requests
import random
import urllib.request
import time
import config

api_key = config.api_key
api_secret = config.api_secret

access_token = config.access_token
token_secret = config.token_secret

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

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name
    urllib.request.urlretrieve(url, full_path)

req = urllib.request.build_opener()
req.addheaders = [{'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}]
urllib.request.install_opener(req)


dl_jpg(img_url, "images/", filename)

def tweet_image():
    interval = 60 * 60 * 3
    
    

    while True:
        print('tweeting kitty pic')
        api.update_with_media("images/" + filename, "here's a kitten <3")
        time.sleep(interval)


tweet_image()
