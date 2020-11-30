'''
Want to look at sentiment about thanksgiving travel: "thanksgiving travel",
"flight", "trip", "travel", "holidays", "road trip", "travel restrictions"

final: "trip", "flight", "travel"



Look at polarity on a state-level
World cloud
Polarity trend each day

'''



# Import the Twython class
from twython import Twython
import json
from textblob import TextBlob

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'thanksgiving',
        'lang': 'en',
        }

import pandas as pd

# Search tweets
dict_ = {'user_loc': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user_loc'].append(status['user']['location'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df['polarity'] = df['text'].apply(lambda tweet: TextBlob(tweet).sentiment.polarity)

df.to_csv('tweets.csv', index=False)
#df.sort_values(by='favorite_count', inplace=True, ascending=False)
#df.head(5)
