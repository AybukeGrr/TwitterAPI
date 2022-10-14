import psycopg2
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"
tweets = []
limit = 10


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
# df.to_csv('tweets.csv')

def sv_database():
    
    conn =  psycopg2.connect(database="twitter", user="postgres", password="aybuke44", host="localhost", port="5432")

    cursor = conn.cursor()
    for t in tweets:
        cursor.execute(
            "INSERT INTO twitterAPI(id, date, username, content)")
    conn.commit()
    print("kayıt başarılı")
    conn.close()

for k in query:
    print(k)
    collect_datas(k)

sv_database()