# [Word Voyage](http://wordvoyage.com/wv-vocabulary) Sample Sentence Fetcher

`Word Voyage` is a website that provides lessons for us to study new vocabulary words. Each lesson normally contains 6 sections: Spelling, Pronunciation, Word Root, Games, Sentence Writing and Quiz, in which Sentence Writing costs a lot of time.

Sentence Writing section lets me write 2 sentences. One from audio and the other by my own. After doing several lessons. I discovered that the sentences are already displayed in `Unit Word Study List`. So, this program written in `Python 3` helps you fetch sentence from a saved `Unit Study List - Word Voyage.html`.

## Optional

To support finding roots, you need to save the finished cousin practice page in order to get root meaning.

## Usage

Run `findword.py`. Then enter the word the lesson requires. This is the possible output of the program

```
Enter the word for sample sentence (empty for exit): mortal
Definition: 1.) Subject to death; destined to die. 2.) Pertaining to man, who is subject to death, or belonging to this world. 3.) Destructive to life; fatal; deadly; dire; relentless. 4.) Pertaining to death.
Roots: base: mori, mort, morti, morti(c) (death; to decay, fail)suffix: al (like, of,  pertaining to, that which)
(The sentence is copied to clipboard)
```

## Prerequisites

You must have the python package `pyperclip` for clipboard support, or the program won't work

You may obtain it by command

    $ pip install pyperclip

## Few words for regex

I really appreciate `regex` because it helps me a lot on searching sentences and vocabulary words in an HTML Document. It really simplifies my program.