# Introduction

This program will:

- get a subreddit's newest posts
- use the natural language tool kit (nltk) to get nouns, verbs, etc. out of the title
- run searches on that subreddit to find similar posts

---------------------------
---------------------------

# Installation

1) Copy the `config.sample.py` and create `config.py`
2) pip install the requirements from requirements.txt

When you run the code for the first time nltk will complain about missing a few dependencies, like "punkt"
to run the importer when nltk complains
```
python
>>> import nltk
>>> nltk.download()
```

Will launch a new window and you can double click the missing dependency to auto download

---------------------------
---------------------------

# Use

`python check.py --subreddit ShowerThoughts --numposts 100 --diff-threshold 20`

will get the most recent 100 posts and, when it finds a candidate repost, print out the results.

provides you with:

- a link to the post (OP) that is our candidate repost
- the title of the post in question
- the important words we found
- the search it will do
- the number of results it found from searching-
- a link to the search results if you want to check them out yourself
- and the similar posts with time stamps that the search resulted in.

## Anatamy of the similar search result printout
`[Timestamp] [Diff Score] <title>`

The lower the diff score the closer to the OP the result is

---------------------------
---------------------------

# Sample outputs and developer comments

You might get a result like this:

-------------------------------------------------------------------------------------------

```
OP:         https://www.reddit.com/r/Showerthoughts/comments/ek1f6d/dogs_are_living_antidepressants/
Title:      Dogs are living antidepressants

Nouns:      ['Dogs', 'antidepressants']
Verbs:      ['are', 'living']
Adjectives: []
Adverbs:    []
Abverbs:    []

Search:     "Dogs living antidepressants"
Results:    2
URL:        https://www.reddit.com/r/ShowerThoughts/search/?restrict_sr=on&q=Dogs%20living%20antidepressants

Similar posts with score under [15]:
 -- [2020-01-04 20:48:52] [0] Dogs are living antidepressants
 -- [2019-07-13 01:34:50] [2] Pets are living antidepressants
```

This one was an extremely similar repost but 6 months apart, it's ok, that kind of repost isn't a problem.
A diff score of [2] is super suspicious, but the time difference is long enough not to care about it.

-------------------------------------------------------------------------------------------

```
OP:         https://www.reddit.com/r/Showerthoughts/comments/ejxnkg/fingerprints_are_human_qr_codes/
Title:      Fingerprints are human QR codes.

Nouns:      ['Fingerprints', 'QR', 'codes']
Verbs:      ['are']
Adjectives: ['human']
Adverbs:    []
Abverbs:    []

Search:     "codes human QR Fingerprints"
Results:    2
URL:        https://www.reddit.com/r/ShowerThoughts/search/?restrict_sr=on&q=codes%20human%20QR%20Fingerprints

Similar posts with score under [15]:
 -- [2020-01-04 16:05:01] [0] Fingerprints are human QR codes.
 -- [2016-02-09 21:26:31] [1] Fingerprints are just human QR codes
```

Again, extremely similar, but 4 years apart.

-------------------------------------------------------------------------------------------

```
OP:         https://www.reddit.com/r/Showerthoughts/comments/ek1k8w/earth_is_the_deadliest_place_on_earth/
Title:      Earth is the deadliest place on Earth.

Nouns:      ['Earth', 'place', 'Earth']
Verbs:      ['is']
Adjectives: ['deadliest']
Adverbs:    []
Abverbs:    []

Search:     "title:is deadliest Earth place"
Results:    3
URL:        https://www.reddit.com/r/ShowerThoughts/search/?restrict_sr=on&q=title%3Ais%20deadliest%20Earth%20place

Similar Posts with score under [15]:
 -- [2020-01-04 20:59:27] [0] Earth is the deadliest place on Earth.
 -- [2018-10-22 18:09:40] [13] The Earth is the deadliest place in the universe, with about 99.99% of all humans dying on it.
 -- [2018-05-29 22:42:01] [12] Earth is the deadliest place in all of existence, because 100% of death occur there
 ```

 This has very similar posts, but I wouldn't call them reposts, they've been worded very differently.

 -------------------------------------------------------------------------------------------

 ```
OP:         https://www.reddit.com/r/Showerthoughts/comments/ejwrr3/actors_who_are_playing_a_scene_where_they_are/
Title:      Actors who are playing a scene where they are pretending to be actors who are acting badly in a scene are actually doing a really good job of acting

Nouns:      ['Actors', 'scene', 'actors', 'scene', 'job']
Verbs:      ['are', 'playing', 'are', 'pretending', 'be', 'are', 'acting', 'are', 'doing', 'acting']
Adjectives: ['good']
Adverbs:    ['badly', 'actually', 'really']
Abverbs:    ['where']

Search:     "actors be actually playing where Actors acting good badly really job doing scene pretending"
Results:    2
URL:        https://www.reddit.com/r/ShowerThoughts/search/?restrict_sr=on&q=actors%20be%20actually%20playing%20where%20Actors%20acting%20good%20badly%20really%20job%20doing%20scene%20pretending

Similar posts with score under [15]:
 -- [2020-01-04 14:43:05] [0] Actors who are playing a scene where they are pretending to be actors who are acting badly in a scene are actually doing a really good job of acting
 -- [2019-02-20 10:22:11] [0] Actors who are playing a scene where they are pretending to be actors who are acting badly in a scene are actually doing a really good job of acting
```

An exact repost, but a year apart

