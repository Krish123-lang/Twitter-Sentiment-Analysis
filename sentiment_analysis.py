# TWEETS
tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

# To get the number of tweets
number_of_tweets = len(tweets)
print(number_of_tweets)

# Let's create two lists of words: happy_words and sad_words. We will use these to check if a tweet is happy or sad.
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

# Taking the first tweet in the tweets list
sample_tweet = tweets[0]
print(sample_tweet)

# To check wether the tweet is happy or not
is_tweet_happy = False

# Get a word from happy_words
for word in happy_words:
    # Check if the tweet contains the word
    if word in sample_tweet:
        # Word found! Mark the tweet as happy
        is_tweet_happy = True
        
        
# Checking the number of happy tweets

# store the final answer in this variable
number_of_happy_tweets = 0

for tweet in tweets:
  for word in happy_words:
    if word in tweet.lower():
      number_of_happy_tweets += 1
      break
print("Number of happy tweets:", number_of_happy_tweets)

# Calculating the fraction of the total number of tweets are happy
# For example, if 2 out of 10 tweets are happy, then the answer is 2/10 i.e. 0.2.
happy_fraction = number_of_happy_tweets/len(tweets)
print("The fraction of happy tweets is:", happy_fraction)

# Determine the number of tweets in the dataset that can be classified as sad.

# store the final answer in this variable

number_of_sad_tweets = 0

for tweet in tweets:
  for word in sad_words:
    if word in tweet:
      number_of_sad_tweets += 1
      break
print("Number of sad tweets:", number_of_sad_tweets)

# Finding the fraction of  total number of tweets are sad.
sad_fraction = number_of_sad_tweets/len(tweets)
print("The fraction of sad tweets is:", sad_fraction)

# Calculating sentiment score i.e happy_fraction - sad_fraction
sentiment_score = happy_fraction - sad_fraction
print("The sentiment score for the given tweets is", sentiment_score)
