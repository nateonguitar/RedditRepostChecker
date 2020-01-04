import praw
import nltk
import urllib.parse
from datetime import datetime
import config

# flags for words, NN == noun
# https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/

# reddit api login
reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    username=config.username,
    password=config.password,
    user_agent=config.user_agent
)

subreddit = reddit.subreddit('Showerthoughts')
new_posts = subreddit.new(limit=500)

keys = {
    'noun':      ('NN', 'NNS', 'NNP', 'NNPS',),
    'verb':      ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ',),
    'adjective': ('JJ', 'JJR', 'JJS',),
    'adverb':    ('RB', 'RBR', 'RBS',),
    'abverb':    ('WRB',),
}
banned_words = ("n't", 't', 's', "'", "’", '"', 'does', 'do', 'are',)

for submission in new_posts:
    try:
        title = submission.title
        tokenized = nltk.word_tokenize(title)
        splits = nltk.pos_tag(tokenized)

        nouns =      [word for (word, pos) in splits if pos in keys['noun']]
        verbs =      [word for (word, pos) in splits if pos in keys['verb']]
        adjectives = [word for (word, pos) in splits if pos in keys['adjective']]
        adverbs =    [word for (word, pos) in splits if pos in keys['adverb']]
        abverbs =    [word for (word, pos) in splits if pos in keys['abverb']]

        # build a string like: see different (colours OR colors)
        
        non_banned_words = [word for word in nouns + verbs + adjectives + adverbs + abverbs if word not in banned_words]
        unique_words = set(non_banned_words)

        # searches of 1 or 2 words never returns any good results, too vague
        if len(unique_words) < 3:
            continue

        search_string = ' '.join(unique_words)

        search_results = subreddit.search(search_string, limit=500)

        posts = []
        for post in search_results:
            posts.append(post)

        if len(posts) > 1: # and num_results < 100:
            print('-------------------------------------------------------------------------------------------')
            print('')
            print('OP:         {}'.format(submission.url))
            print('Title:      {}'.format(title))
            print('')
            print('Nouns:      {}'.format(nouns))
            print('Verbs:      {}'.format(verbs))
            print('Adjectives: {}'.format(adjectives))
            print('Adverbs:    {}'.format(adverbs))
            print('Abverbs:    {}'.format(abverbs))
            print('')
            print('Search:     "{}"'.format(search_string))
            print('Results:    {}'.format(len(posts)))
            print('URL:        https://www.reddit.com/{}?restrict_sr=on&q={}'.format(search_results.url, urllib.parse.quote(search_string)))
            print('')
            print('First 10:')
            i = 0
            for post in posts:
                print(' -- [{}] {}'.format(datetime.fromtimestamp(post.created), post.title))
                i += 1
                if i == 10:
                    break
            print('')

    except Exception as e:
        print(e)
