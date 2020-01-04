import praw
import nltk
import urllib.parse
from datetime import datetime
import config
import argparse
import difflib

def diff(s1, s2):
    ''' --word-diff=porcelain clone'''
    delta = difflib.Differ().compare(s1.split(), s2.split())
    difflist = []
    fullline = ''
    for line in delta:
        if line[0] == '?':
            continue
        elif line[0] == ' ':
            fullline += line.strip() + ' '
        else:
            if fullline:
                difflist.append(fullline[:-1])
                fullline = ''
            difflist.append(line)
    if fullline:
        difflist.append(fullline[:-1])
    return [l[:] for l in '\n'.join(difflist).splitlines() if l]

parser = argparse.ArgumentParser(description='Reddit Repost Checker')
parser.add_argument("--subreddit", required=True, default=None, type=str, help="The subreddit you would like to search")
parser.add_argument("--numposts", default=100, type=int, help="The number of posts you want to test.")
parser.add_argument("--diff-threshold", default=15, type=int, help="The threshold of the diff_score, the higher the more results you'll see printed out.")

args = parser.parse_args()

print('')
print("Subreddit:      {}".format(args.subreddit))
print("Num Posts:      {}".format(args.numposts))
print("Diff Threshold: {}".format(args.diff_threshold))
print('')

# reddit api login
reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    username=config.username,
    password=config.password,
    user_agent=config.user_agent
)

subreddit = None
try:
    subreddit = reddit.subreddit(args.subreddit)
except Exception as e:
    print(e)
    quit()

new_posts = subreddit.new(limit=args.numposts)

# flags for words, NN == noun
# https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/
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
        
        words = nouns + verbs + adjectives + adverbs + abverbs
        non_banned_words = [word for word in words if word not in banned_words]
        unique_words = set(non_banned_words)

        # searches of 1 or 2 words never returns any good results, too vague
        if len(unique_words) < 2:
            print('.', end='')
            continue

        # only search the titles
        search_string = 'title:{}'.format(' '.join(unique_words))

        search_results = subreddit.search(search_string, limit=500)

        posts = []
        for post in search_results:
            posts.append(post)

        if len(posts) > 1: # and num_results < 100:
            similar_diff_posts = []
            for post in posts:
                # diffs that contain a + or a -, meaning an actual diff.
                diffs = diff(title, post.title)
                diff_score = len([word for word in diffs if '+' in word or '-' in word])
                if diff_score < args.diff_threshold:
                    similar_diff_posts.append({
                        'title': post.title,
                        'timestamp': datetime.fromtimestamp(post.created),
                        'diff_score': diff_score,
                    })

            if len(similar_diff_posts) > 1:
                print('')
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
                print('Similar Posts with score under [{}]:'.format(args.diff_threshold))
                for p in similar_diff_posts:
                    print(' -- [{}] [{}] {}'.format(p['timestamp'], p['diff_score'], p['title']))
                print('')
            else:
                print('.', end='')
        else:
            print('.', end='')
    except Exception as e:
        print(e)
