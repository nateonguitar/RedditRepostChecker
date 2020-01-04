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