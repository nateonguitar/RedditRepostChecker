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

`python check.py --subreddit ShowerThoughts` will, when it finds a candidate repost, print something like this:

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

It provides you with:

- a link to the post (OP) that is our candidate repost
- the title of the post in question
- the important words we found
- the search it will do
- the number of results it found from searching-
- a link to the search results if you want to check them out yourself
- and the first 10 posts with time stamps that the search resulted in.