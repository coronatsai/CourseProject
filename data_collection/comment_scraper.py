"""
This file scrapes comment data related the filtered threads in cleaned_data/threads.csv

This file relies on cleaned_data/threads.csv existing.

It creates/overwrites csv file with the following headings:
    comments.csv: subreddit_id,comment,created_utc
"""
import json
import praw
from praw.models import MoreComments
import csv
import io
import pandas as pd
import numpy as np
import requests

data_outfolder = "raw_data/"

# You should have a file containing your reddit credentials
# This file should never be shared /or pushed to git
credentials_file = "../.secrets/credentials.json"
with open(credentials_file) as f:
    params = json.load(f)

reddit = praw.Reddit(client_id=params['client_id'],
                     client_secret=params['api_key'],
                     password=params['password'],
                     user_agent='cs410test',
                     username=params['username'])

# Collect comment data:

comments_outfile = data_outfolder + "comments.csv"

threads_datafile = "cleaned_data/threads.csv"

# Threads data
# threads_df = pd.read_csv(threads_datafile) // Too many threads in the cleaned data, better to filter by a smaller time frame or by keywords next time
# thread_ids = threads_df['thread_id']

# Manually go through cleaned_data threads.csv, select thread_ids that look relevant to your game
thread_ids = ['qo0hlw','qn77pm','q58hok','qlpvja','qo4gxm','qo5dwg','qon5e0','qptyyp']
with io.open(comments_outfile, 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)

    # column labels
    writer.writerow(["comment", "created_utc"])

    for tid in thread_ids:
        # Submission id comes after comment/ in the URL
        submission = reddit.submission(id=tid)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            writer.writerow([
                comment.body,
                comment.created_utc
            ])
