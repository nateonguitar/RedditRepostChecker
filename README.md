## Introduction

This program will:

- get a subreddit's newest posts
- use the natural language tool kit (nltk) to get nouns, verbs, etc. out of the title
- run searches on that subreddit to find similar posts


## Installation

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

## Use

`python check.py --subreddit ShowerThoughts --numposts 100`

will get the most recent 100 posts and, when it finds a candidate repost, print something like this:

provides you with:

- a link to the post (OP) that is our candidate repost
- the title of the post in question
- the important words we found
- the search it will do
- the number of results it found from searching-
- a link to the search results if you want to check them out yourself
- and the first 10 posts with time stamps that the search resulted in.

## Sample outputs and developer comments

You might get a result like this:

```
-------------------------------------------------------------------------------------------

OP:         https://www.reddit.com/r/Showerthoughts/comments/ejzajo/a_natural_museum_is_a_zoo_for_dead_animals/
Title:      A natural museum is a zoo for dead animals.

Nouns:      ['museum', 'zoo', 'animals']
Verbs:      ['is']
Adjectives: ['natural', 'dead']
Adverbs:    []
Abverbs:    []

Search:     "museum natural zoo is dead animals"
Results:    2
URL:        https://www.reddit.com/r/ShowerThoughts/search/?restrict_sr=on&q=museum%20natural%20zoo%20is%20dead%20animals

First 10:
 -- [2020-01-04 18:14:18] A natural museum is a zoo for dead animals.
 -- [2018-06-30 06:14:14] A natural history museum is just a dead animal zoo
```

 This one was an extremely similar repost but a year and a half apart, it's ok, that kind of repost isn't a problem.


```
-------------------------------------------------------------------------------------------

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

First 10:
 -- [2020-01-04 16:05:01] Fingerprints are human QR codes.
 -- [2016-02-09 21:26:31] Fingerprints are just human QR codes
```

Again, extremely similar, but 4 years apart.

```
-------------------------------------------------------------------------------------------

OP:         https://www.reddit.com/r/Showerthoughts/comments/ejy5ii/life_is_pay_2_win/
Title:      Life is pay 2 win

Nouns:      ['Life', 'win']
Verbs:      ['is', 'pay']
Adjectives: []
Adverbs:    []
Abverbs:    []

Search:     "Life win pay is"
Results:    187
URL:        https://www.reddit.com/r/ShowerThoughts/search/?restrict_sr=on&q=Life%20win%20pay%20is

First 10:
 -- [2019-02-13 22:36:01] Life is pay to win but the currency used to buy In-game currency is In-game currency
 -- [2019-12-05 18:04:59] Your life is a pay to win rpg and your stats are randomly generated
 -- [2020-01-04 16:46:43] Life is pay 2 win
 -- [2019-10-28 18:02:52] Healthy food costing more than fast food is a real life example of pay-to-win.
 -- [2019-12-14 23:14:14] Life is pay-to-win. If you don’t pay for stuff like food or water, you’ll just die- or lose.
 -- [2019-12-19 21:09:35] Life is the epitome of pay-to-win. You can go through life normally, but having money unlocks features that make it easier.
 -- [2019-12-26 17:48:11] Life is a pay to win game
 -- [2019-12-07 01:04:47] Life is actually not pay-to-win because to get rich you just have to grind for in-game currency.
 -- [2019-11-27 11:58:58] Pay to win games are actually the most realistic since that is literally how life works.
 -- [2019-12-12 09:06:11] Life is pay to win with a ton of microtransactions.
 ```

 This has a TON of very similar posts, but I wouldn't call them reposts, they've been worded very differently.

 ```
 -------------------------------------------------------------------------------------------

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

First 10:
 -- [2020-01-04 14:43:05] Actors who are playing a scene where they are pretending to be actors who are acting badly in a scene are actually doing a really good job of acting
 -- [2019-02-20 10:22:11] Actors who are playing a scene where they are pretending to be actors who are acting badly in a scene are actually doing a really good job of acting
```

An exact repost, but a year apart

