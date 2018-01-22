import re
import json

content=""

with open("Unit Study List - Word Voyage.html") as f:
    content=f.read()
rmhtml = re.compile("<[^>]*>")
word=re.compile("\S+\s+Definition:")
word2=re.compile("[a-z]+")
sentence = re.compile("Sample sentence: ([^.]+\.)")
text = re.sub(rmhtml, "", str(content))
rs=word.findall(text)
words=[]
dict={}
for w in rs:
    wx=re.search(word2,w).group(0)
    words.append(wx)
sentences=sentence.findall(text)
for index,w in enumerate(words):
    dict[w]=sentences[index]
with open("sentences.json","w") as file:
    json.dump(dict,file)
print("Sample sentence saved")