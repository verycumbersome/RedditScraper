import praw
import json

class RedditScraper:
    def __init__(self):
        self.photo_urls = []

        with open('credentials.json') as auth_data:
            credentials = json.load(auth_data)

            self.reddit = praw.Reddit(client_id=credentials['client_id'],
                                 client_secret=credentials['client_secret'],
                                 password=credentials['password'],
                                 user_agent='Reddit image scraper',
                                 username=credentials['username'])


    def get_subreddit_images(self, subreddit, limit):
        for submission in self.reddit.subreddit(subreddit).hot(limit=limit):
            self.photo_urls.append(submission.url)

        return self.photo_urls

if __name__ == '__main__':
    scraper = RedditScraper()

    scraper.get_subreddit_images('me_irl', 25)
