import tweepy
import requests
import pandas as pd
from io import StringIO
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler




consumer_key_apikey='HpmqAfVOB8kPf8zYJhGQ8pqSx'
consumer_secret='4nIEX7lnngFHtY60dMTRjesogAXJKuJF71cTA1GIWXn2vTPR2f'

access_token='2739037084-oFuQL2TOYZOYmiZ3XnyyuabXZkatJ7XMm8ygIZt'
access_token_secret='1TS3FKODyJnxSK7N9mXMdNeUoXkH1sPUmNVeyfI0lKYMv'

auth = tweepy.OAuthHandler(consumer_key_apikey, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=1)
def timed_job():
    print('This job is run every 24 hours.')
    # SELECT new_cases.date,* FROM new_cases ORDER BY new_cases.date DESC LIMIT 1
    r = requests.get('https://download.data.world/s/34tql5uiukwqrpz7u6tfal54pfqsk4')

    print("Today is: ", date.today())
    df = pd.read_csv(StringIO(r.text), sep=",")
    data = df['date'].values
    print("Date from df: ", data)
    df = df.drop('world', axis=1)
    df = df.drop('date', axis=1)
    df = df.drop('date_2', axis=1)
    df = df.drop('europe', axis=1)
    df = df.drop('european_union', axis=1)
    df = df.drop('north_america', axis=1)
    df = df.drop('south_america', axis=1)
    df = df.drop('asia', axis=1)
    df['COLUMN_I_WANT_TO_CREATE'] = df.idxmax(axis=1)
    most_cases_nation = df['COLUMN_I_WANT_TO_CREATE']
    worst = df['COLUMN_I_WANT_TO_CREATE'].values
    print(worst)
    print(df[worst].values)
    api.update_status("CovidBot! The country that has more infections today " + data + " : " + worst + ", is " + str(df[worst].values) +"   #covid" )


sched.start()

