from html2text import html2text
import re


def getwords():
    f=open("Unit Study List - Word Voyage.html")
    text=html2text(f.read())
    f.close()
    word=re.compile("([a-z]+)\s+Definition:")
    return word.findall(text)
