"""
This file analyzes the sentiments regarding teams and their players

It generates/updates several graphs which may be found in the same directory as the script.
"""
import numpy as np
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

datafile = 'data_collection/cleaned_data/data.csv'
## team names and 5 starting players from each team
team1 = "DK"
team2 = "EDG"

num_players = 5

t1_players = ["Khan", "Canyon", "ShowMaker", "Ghost", "BeryL"]
t2_players = ["Flandre", "Jiejie", "Scout", "Viper", "meiko"]
combined_player_list = t1_players + t2_players

t1_playersentiments = []
t2_playersentiments = []
# hold onto sentiment values from going through the data
t1_sentiments = [[],[],[],[],[]]
t2_sentiments = [[],[],[],[],[]]

# load in the combined thread and comment data
data = pd.read_csv(datafile)

# Go through data and find text referencing the players
for text in data['text']:
    for player in t1_players:
        if (player in text):
            text_sentiment = TextBlob(text).sentiment
            # print(text_sentiment)
            index = t1_players.index(player)
            if (t1_sentiments[index] == []):
                t1_sentiments[index] = [text_sentiment]
            else:
                t1_sentiments[index].append(text_sentiment)

    for player in t2_players:
        if (player in text):
            text_sentiment = TextBlob(text).sentiment
            index = t2_players.index(player)
            if (t2_sentiments[index] == []):
                t2_sentiments[index] = [text_sentiment]
            else:
                t2_sentiments[index].append(text_sentiment)
#
# print(t1_sentiments)
# print(t1_sentiments[0])
# For sorting team player sentiment
def sentiment_element(element):
    return element[1]

# Count and average sentiments per player
threshold = 0.10
i = 0
for player_sentiments in t1_sentiments:
    sentiment_count = 0
    sentiment_total = 0
    # print(player_sentiments)
    for sentiment in player_sentiments:
        # print(sentiment)
        if (sentiment[1] >= threshold):
            sentiment_count += 1
            sentiment_total = sentiment_total + sentiment[0]

    if (sentiment_total == 0):
        t1_playersentiments.append([t1_players[i], 0, sentiment_count])
    else:
        t1_playersentiments.append([t1_players[i], sentiment_total / sentiment_count, sentiment_count])
    i += 1
t1_playersentiments.sort(key=sentiment_element)
# for team 2
i = 0
for player_sentiments in t2_sentiments:
    sentiment_count = 0
    sentiment_total = 0
    for sentiment in player_sentiments:
        if (sentiment[1] >= threshold):
            sentiment_count += 1
            sentiment_total = sentiment_total + sentiment[0]
    if (sentiment_total == 0):
        t2_playersentiments.append([t2_players[i], 0, sentiment_count])
    else:
        t2_playersentiments.append([t2_players[i], sentiment_total / sentiment_count, sentiment_count])
    i += 1
t2_playersentiments.sort(key=sentiment_element)

# Team indices
t1_index = []
t2_index = []
t1_sentiment = []
t2_sentiment = []

for x in t1_playersentiments:
    t1_index.append(x[0])
    t1_sentiment.append(round(x[1], 2))
for x in t2_playersentiments:
    t2_index.append(x[0])
    t2_sentiment.append(round(x[1], 2))

# Enable interactive mode
plt.ion()

team1_outfile = 'team1_sentiment.png'
team2_outfile = 'team2_sentiment.png'

def plot_team_sentiment(index, sentiment, color, team, outfile):
    fig, ax = plt.subplots()
    ax.barh(index, sentiment, color=color)
    plt.title(team + ' Sentiment')
    plt.xlabel('Sentiment Score')
    for i, j in enumerate(sentiment):
        ax.text(j, i, " " + str(j), color='black', va='center', fontweight='bold')
    plt.savefig(outfile)

plot_team_sentiment(t1_index, t1_sentiment, 'blue', team1, team1_outfile)
plot_team_sentiment(t2_index, t2_sentiment, 'red', team2, team2_outfile)
