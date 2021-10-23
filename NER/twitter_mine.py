from twython import Twython
import json
import pandas as pd

# Load credentials from json file
with open("credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'to%3ASafaricom_Care',
         'result_type': 'recent',
         'lang': 'en',
         'include_entities': 'true'
         }

# Create a dict object to keep track of the tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'location': [], 'hashtags': []}


# Run the search API call
for status in python_tweets.search(**query)['statuses']:
    # Add the data we would like
    dict_['hashtags'].append(status['entities']['hashtags'])
    dict_['user'].append(status['user']['screen_name'])
    dict_['location'].append(status['user']['location'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Convert to a dataframe
df = pd.DataFrame(dict_)

# dropping ALL duplicate values
df.drop_duplicates(subset="text", inplace=True)

df.to_csv('data.csv', index=False)

