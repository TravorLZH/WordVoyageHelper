from html2text import html2text
import re

def getroots():
    try:
        with open("Word Discovery - Learn - Word Voyage.html") as f:
            content = f.read()
    except FileNotFoundError:
        return ""
    content = re.sub(r'<head>.*</head>', "", content, flags=re.DOTALL)
    d=r'<div id="openModal\d+" class="modalDialog">.*?(?<=</div><!-- end OpenModal2 -->)'
    x=re.findall(d, content, re.DOTALL)
    d={}
    for a in x:
        xx=re.search(r'<div class="title">(\w+)</div>',a)
        title=xx.group(1)
        xx=re.search(r'<h3>Roots:</h3>\s+<ul>\s+(.*?)\s+</ul>', a, re.DOTALL)
        d[title]=html2text(xx.group(1))
    return d

def getbasemeaning(r):
    return re.search(r'base:.*?\((.*?)\)suffix', r).group(1)
