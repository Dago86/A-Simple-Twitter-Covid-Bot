# A-Simple-Twitter-Covid-Bot
A Twitter bot written using the Tweepy library and collecting statistics from the data.world site

## Installation

You can install install packages easily:
First, activate your venv, then write in your shell
```bash
pip install -r requirements.txt
```


This bot takes care of doing a twit every 24 hours in which the nation with the highest number of infections writes on the last date present. The dataset used is the [Coronavirus Daily Data](https://data.world/markmarkoh/coronavirus-data) file available on the data.world site. I wrote a simple SQL query from the integrated [data.world](https://data.world/) engine that allows you to extract the latest update on all the countries present in the excel file.

The bot was written using the [Tweepy](https://www.tweepy.org/) library.
Remember, however, before registering on the [Twitter Developer](https://developer.twitter.com/en/apply-for-access) portal to be able to access the authentication keys, which in the code, for obvious privacy issues, I have deleted.
```bash
consumer_key_apikey=''
consumer_secret=''

access_token=''
access_token_secret=''
```
