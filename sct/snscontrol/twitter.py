from twitter import Twitter,OAuth
from dotenv import load_dotenv
import os

class TwitterUtil:

    auth = None

    def __init__(self) -> None:
        load_dotenv()
        self.auth = OAuth(
            consumer_key=os.getenv('CONSUMER_KEY'),
            consumer_secret=os.getenv('CONSUMER_SECRET'),
            token=os.getenv('TWITTER_TOKEN'),
            token_secret=os.getenv('TWITTER_TOKEN_SECRET'))



    def post(self, text):
        tw = Twitter(auth=self.auth)
        tw.statuses.update(status=text)

    def post_with_media(self, text, media_ids):
        tw = Twitter(auth=self.auth)
        tw.statuses.update(status=text,media_ids=media_ids)

class TwitterUpload:

    twi = None
    
    def __init__(self) -> None:
        load_dotenv()
        
        self.twi = Twitter(
            domain='upload.twitter.com',
            auth=OAuth(
                consumer_key=os.getenv('CONSUMER_KEY'),
                consumer_secret=os.getenv('CONSUMER_SECRET'),
                token=os.getenv('TWITTER_TOKEN'),
                token_secret=os.getenv('TWITTER_TOKEN_SECRET')))
    
    def upload_media(self,imagedata):
        id_img1 = self.twi.media.upload(media=imagedata)["media_id_string"]

        return id_img1