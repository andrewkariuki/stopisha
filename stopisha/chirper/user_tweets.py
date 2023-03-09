import json

import tweepy

from stopisha.core.config import config

consumer_key = config.TWITTER_API_KEY
consumer_secret = config.TWITTER_API_KEY_SECRET
access_token = config.TWITTER_ACCESS_TOKEN
access_secret = config.TWITTER_ACCESS_SECRET


def get_all_tweets(screen_name):
    """
    Twitter only allows access to a users most recent 3240 tweets with this method

    Authorize twitter, by initializing tweepy

    Initialize a list to hold all the tweepy Tweets

    Make initial request for most recent tweets (200 is the maximum allowed count)
    """

    if (
        str(consumer_key).strip() == ""
        or str(consumer_secret).strip() == ""
        or str(access_token).strip() == ""
        or str(access_secret).strip() == ""
    ):
        print("API key not found. Please .env file")
        return
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    alltweets = []
    new_tweets = api.user_timeline(
        screen_name=screen_name, count=200, tweet_mode="extended"
    )
    # Save most recent tweets
    alltweets.extend(new_tweets)
    # Save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    # Keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        # All subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(
            screen_name=screen_name, count=200, max_id=oldest, tweet_mode="extended"
        )
        # save most recent tweets
        alltweets.extend(new_tweets)
        # Update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
    print(f"...{len(alltweets)} tweets downloaded so far")
    with open(f"{screen_name}.json", "w", encoding="utf-8") as outfile:
        for t in alltweets:
            outfile.write(json.dumps(t._json))
            outfile.write("\n")
    print(
        f"{len(alltweets)} tweets have been written successfully to {screen_name}.json"
    )


# def process_json(screen_name):
#     workbook = xlsxwriter.Workbook('%s_tweets.xlsx' % screen_name)
#     worksheet = workbook.add_worksheet()
#     # Start from the first cell. Rows and columns are zero indexed.
#     row = 0
#     col = 0
#     worksheet.write(row, 0, 'id')
#     worksheet.write(row, 1, 'created_at')
#     worksheet.write(row, 2, 'full_text')
#     worksheet.write(row, 3, 'clean_text')
#     row += 1

#     with open(f'{screen_name}.json', 'w', encoding="utf-8") as json_reader:
#         lines = json_reader.readlines()
#         for line in lines:
#             json_tweet = json.loads(line)

#             if 'retweeted_status' in json_tweet:
#                 text = json_tweet['retweeted_status']['full_text']
#             else:
#                 text = json_tweet['full_text']

#             clean_text = tweet_cleaner.clean_tweet(text)
#             clean_text = tweet_cleaner.normalize_arabic(clean_text)
#             clean_text = tweet_cleaner.remove_repeating_char(clean_text)
#             clean_text = tweet_cleaner.keep_only_arabic(clean_text.split())
#             worksheet.write(row, col, json_tweet['id_str'])
#             worksheet.write(row, col + 1, json_tweet['created_at'])
#             worksheet.write(row, col + 2, text)
#             worksheet.write(row, col + 3, clean_text)
#             row += 1
#         workbook.close()
