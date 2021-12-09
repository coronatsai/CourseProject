"""
This file scrapes data related to the following subreddits:
    Regions: ["leagueoflegends", "LEC_lol", "lck", "LCS", "lplcn"]

It creates/overwrites 2 files csv files with the following headings:
    subreddits.csv: subreddit_id,display_name,created_utc,subscribers
    threads.csv: subreddit_id,thread_id,title,created_utc,author,num_comments,upvote_ratio,link
    comments.csv: subreddit_id,comment,created_utc
"""
import json
import praw
import csv
import io
import pandas as pd
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


# Collect subreddit data:

subreddit_outfile = data_outfolder + "subreddits.csv"
subreddit_names = ["leagueoflegends", "LEC_lol", "lck", "LCS", "lplcn"]

# Note this overwrites the file if it already exists
with io.open(subreddit_outfile, 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)

    # column labels
    writer.writerow(["subreddit_id", "display_name", "created_utc", "subscribers"])

    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)
        writer.writerow([
            subreddit.id,
            subreddit.display_name,
            subreddit.created_utc,
            subreddit.subscribers])


# Collect submission (thread) data:

threads_outfile = data_outfolder + "threads.csv"

with io.open(threads_outfile, 'w', newline='',encoding="utf-8") as file:
    writer = csv.writer(file)

    # column labels
    writer.writerow(["subreddit", "subreddit_id", "thread_id", "title", "created_utc", "author", "num_comments", "upvote_ratio", "link"])

    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)

        for submission in subreddit.top(limit=None):
            submission_created = pd.to_datetime(submission.created_utc, unit="s")

            writer.writerow([
                subreddit.display_name,
                subreddit.id,
                submission.id,
                submission.title,
                submission.created_utc,
                submission.author,
                submission.num_comments,
                submission.upvote_ratio,
                submission.url])
