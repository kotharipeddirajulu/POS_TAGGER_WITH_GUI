# POS_TAGGER_WITH_GUI
This is a project based on POS tagging using TextBlob Library and a simple Gui using Tkinter

TextBlob module is used for building programs for text analysis. One of the more powerful aspects of the TextBlob module is the Part of Speech tagging.

### Install TextBlob run the following commands:

``` 
    $ pip install -U textblob
    $ python -m textblob.download_corpora 
 ```

This will install TextBlob and download the necessary NLTK corpora.
The above installation will take quite some time due to the massive amount of tokenizers, chunkers, other algorithms, and all of the corpora to be downloaded.

- ***Corpus***: Body of text, singular. Corpora is the plural of this.
- ***Lexicon*** : Words and their meanings.
- ***Token*** : Each “entity” that is a part of whatever was split up based on rules.

##### In corpus linguistics, part-of-speech tagging (POS tagging or PoS tagging or POST), also called Grammatical tagging or Word-category disambiguation.

```
Input: Everything is all about money.
Output: [('Everything', 'NN'), ('is', 'VBZ'), 
              ('all', 'DT'), ('about', 'IN'), 
                             ('money', 'NN')] 
```

***Here’s a list of the tags, what they mean, and some examples:***
####
```
CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent‘s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO to go ‘to‘ the store.
UH interjection errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when
```
####

> Basically, the goal of a POS tagger is to assign linguistic (mostly grammatical) information to sub-sentential units. Such units are called tokens and, most of the time, correspond to words and symbols (e.g. punctuation).

### GUI using Tkinter ###

Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python. It is a standard Python interface to the Tk GUI toolkit shipped with Python. As Tk and Tkinter are available on most of the Unix platforms as well as on the Windows system, developing GUI applications with Tkinter becomes the fastest and easiest.

