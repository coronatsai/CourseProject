"""
Filter thread data by date

Expects the following files to exist:
    raw_data/threads.csv

Output file and column names:
    cleaned_data/threads.csv
        subreddit
        thread_id
        title
        date
"""
import numpy as np
import pandas as pd

threads_datafile = "raw_data/threads.csv"
outfile = "cleaned_data/threads.csv"

# Threads data
threads_df = pd.read_csv(threads_datafile)

# Select start and end dates to filter by.
start_date = '2021-10-10' #YYYY,MM,DD
end_date = '2021-11-13'

output_df = threads_df.filter(['subreddit', 'thread_id', 'title', 'created_utc'])
output_df['date'] = pd.to_datetime(output_df['created_utc'], unit='s')
output_df = output_df.drop(['created_utc'], axis = 1)

# Filter threads to only include those falling between the start_date and end_date, inclusive
output_df = output_df[(output_df['date'] > pd.to_datetime(start_date))&(output_df['date'] <= pd.to_datetime(end_date))]

output_df = output_df.sort_values(by='date')

# Save to CSV
output_df.to_csv(outfile, index=False, header=True)
