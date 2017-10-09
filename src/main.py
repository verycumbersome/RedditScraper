from reddit_scraper import RedditScraper
import urllib


if __name__=='__main__':
    scraper = RedditScraper()

    photo_urls = scraper.get_subreddit_images('comedycemetery', 25)

    for photo_id, photo_url in enumerate(photo_urls):
        urllib.urlretrieve(photo_url, 'images/'+str(photo_id)+'.jpg')
