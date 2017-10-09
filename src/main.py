import praw
import json

with open('credentials.json', 'rw') as credentials:
    reddit = praw.Reddit(client_id=credentials['client_id'],
                         client_secret=credentials['client_secret'],
                         password=credentials['password'],
                         user_agent='Reddit image scraper',
                         username=credentials['username'])
