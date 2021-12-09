# CS410 Course Project Documentation

Refer to the section about running the reddit data scraper for more about how the data was collected, cleaned and filtered.
Refer to the section titled 'Running the sentiment analysis' to run the script yourself. Further code documentation is included within the code comments.

### Running the reddit data scraper
The data is retrieved through Praw and in order to run the data scraper to create/update the data to include recent posts, you will need to have python3, praw and pandas installed.
If either are not yet installed, please run `pip install praw` or `pip install pandas` to install.

1. follow the instructions here <https://towardsdatascience.com/exploring-reddits-ask-me-anything-using-the-praw-api-wrapper-129cf64c5d65> and set up a .secrets folder containing your credentials. the .secrets folder should be in the same directory containing the data_collection directory. do not commit your .secrets folder
2. run the following command from the data_collection directory
```
python data_scraper.py
```
After running this command, the raw_data will be updated to include the latest activity from the visualization related subreddits.

3. run the following command from the data_collection directory
```
python data_cleaning.py
```
After running this command, the raw_data will be filtered by dates specified. Columns kept include date, title and subreddit.
4. run the following command from the data_collection directory
```
python comment_scraper.py
```
After running this command, comments from specified threads will be scraped and written into raw_data/comments.csv
This command may take some time to run. Currently, threads are manually specified from looking at thread titles in threads.csv
5. run the following command from the data_collection directory
```
python data_combine.py
```
After running this command, the comment body from comments.csv and titles from cleaned_data/threads.csv will be joined. This will create/update cleaned_data/data.csv

### Running the sentiment analysis
After specifying two teams of interest as well as listing their roster, sentiment analysis will be performed on the relevant text through textblob. You will need to have pandas, textblob, and matplotlib installed for this.
Use pip install to install any missing packages.

1. run the sentiment analysis script from the same directory as the readme. This script will perform sentiment analysis on the cleaned_data/data.csv and generate two graphs showing the sentiment analysis of threads and comments mentioning player names. These graphs will be created/updated every time the script is ran.
```
python sentiment_analysis.py
```
After running this command, team1_sentiment.png and team2_sentiment.png should be created/updated.
