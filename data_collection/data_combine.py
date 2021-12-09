"""
Filter thread data by date

Expects the following files to exist:
    raw_data/threads.csv

Output file and column names:
    cleaned_data/data.csv
        text
        date
"""
import numpy as np
import pandas as pd

threads_datafile = "cleaned_data/threads.csv"
comments_datafile = "raw_data/comments.csv"
outfile = "cleaned_data/data.csv"

# Threads data
threads_df = pd.read_csv(threads_datafile)
threads_df = threads_df.drop(['subreddit'], axis=1)
threads_df = threads_df.drop(['thread_id'], axis=1)

start_date = '2021-11-05' # 2 days before the finals
end_date = '2021-11-10' # 3 days after

# Comments data
comments_df = pd.read_csv(comments_datafile)

comments_df['date'] = pd.to_datetime(comments_df['created_utc'], unit='s')
comments_df = comments_df.drop(['created_utc'], axis = 1)
comments_df = comments_df[(comments_df['date'] > pd.to_datetime(start_date))&(comments_df['date'] <= pd.to_datetime(end_date))]

threads_df.rename(columns = {'title':'text'}, inplace=True)
comments_df.rename(columns = {'comment':'text'}, inplace=True)

# Append two dfs into 1 df
output_df = pd.concat([threads_df, comments_df], ignore_index=True)

# Save to CSV
output_df.to_csv(outfile, index=False, header=True)
