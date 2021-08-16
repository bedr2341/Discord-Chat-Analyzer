import pandas as pd

channels = ['general', 'asu', 'news', 'random', 'youtube-mix-tapes', 'rant', 'debate', 'oc_memes',
            'memes', 'tech', 'coding', 'sports', 'gaming', 'food', 'auto', 'movies_tv', 'literature', 'photography']


# This gets all the user's messages
def getAllUserMessages(df, authorName):
    return df.loc[df["Author"] == authorName]

# This searches for a user's exact message
def searchExactUserMessages(df, authorName, messageString):
    return df.loc[(df["Author"] == authorName) & (df["Content"] == messageString)]

# This searhes for a substring in all user's messages
def searchPartialUserMessage(df, authorName, messageString):
    return df.loc[(df["Author"] == authorName) & (df["Content"].str.contains(messageString))]

if __name__ == "__main__":
    arya_authorName = 'Trail-_-Blazer#7237'
    generalDF = pd.read_csv('./data/general.csv')

    print(searchPartialUserMessage(generalDF, arya_authorName, "haha"))
    # print(searchExactUserMessages(generalDF, arya_authorName, "hahaha"))