import re
from html2text import html2text
from getwords import getwords


def getdefinitions():
    with open("Unit Study List - Word Voyage.html") as f:
        content=f.read()
    definition = re.compile("Definition: ([^\n]+)", re.MULTILINE)
    text=html2text(str(content))
    dic={}
    words=getwords()
    defs=definition.findall(text)
    for index,w in enumerate(words):
        dic[w]=defs[index]
    return dic