import re
from html2text import html2text
from getwords import getwords


def getsentences():
    with open("Unit Study List - Word Voyage.html") as f:
        content=f.read()
    sentence = re.compile("Sample sentence: ([^.]+\.)")
    text=html2text(str(content))
    dic={}
    words=getwords()
    sentences=sentence.findall(text)
    for index,w in enumerate(words):
        dic[w]=sentences[index]
    return dic
