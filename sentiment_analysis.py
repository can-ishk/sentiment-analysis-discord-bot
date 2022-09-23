from distutils.command.config import config
import os
from dotenv import load_dotenv
load_dotenv()
import boto3
from botocore.config import Config

key = os.getenv('AWS_ACCESS_KEY_ID')
secret = os.getenv('AWS_SECRET_ACCESS_KEY')
my_config = Config(
    region_name = 'ap-south-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)


client = boto3.client('comprehend', aws_access_key_id=key, aws_secret_access_key=secret, config=my_config)

def sentiment_analysis(text):
    response = client.detect_sentiment(Text=text, LanguageCode='en')
    sentiment = response['Sentiment']
    return sentiment

def is_greeting(text):
    response = client.detect_syntax(Text=text, LanguageCode='en')
    for word in response['SyntaxTokens']:
        if word['PartOfSpeech']['Tag'] == 'INTJ' and word['PartOfSpeech']['Score']>0.6:
            return True