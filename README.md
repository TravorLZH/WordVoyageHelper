# [Word Voyage](http://wordvoyage.com/wv-vocabulary) Sample Sentence Fetcher

`Word Voyage` is a website that provides lessons for us to study new vocabulary words. Each lesson normally contains 6 sections: Spelling, Pronunciation, Word Root, Games, Sentence Writing and Quiz, in which Sentence Writing costs a lot of time.

Sentence Writing section lets me write 2 sentences. One from audio and the other by my own. After doing several lessons. I discovered that the sentences are already displayed in `Unit Study List`. So, this program written in `Python 3` helps you fetch sentence from a saved `Unit Study List - Word Voyage.html`.

## Usage

Run `findword.py`. Then enter the word the lesson requires. This is the possible output of the program

```
Enter the word for sample sentence (empty for exit): abide
1.) To endure without yielding; to bear patiently; to accept without objection; to put up with. 2.) To wait; to pause; to delay. 3.) To stay; to continue in a place; to have one's abode; to dwell; with with before a person, and commonly with at or in before a place. 4.) To remain stable or fixed in some state or condition; to continue; to remain.
(The sentence is copied to clipboard)
```

## Prerequisites

You must have the python package `pyperclip` for clipboard support, or the program won't work

You may obtain it by command

    $ pip install pyperclip

## Few words for regex

I really appreciate `regex` because it helps me a lot on searching sentences and vocabulary words in an HTML Document. It really simplifies my program.