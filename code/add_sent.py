#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--date',required=True)
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
import pandas as pd
from textblob import TextBlob


df = pd.read_csv(args.date + '.csv', error_bad_lines=False, encoding='utf-8 ', engine='python')

print(df['text'])

df['polarity'] = df.apply(lambda tweet: TextBlob(tweet['text']).sentiment.polarity, axis=1)

df.to_csv('sample.csv', index=False)

