import pyperclip
from getsentences import getsentences
from getdefinitions import getdefinitions
from getroots import *

dic = getsentences()
dic2 = getdefinitions()
roots = getroots()
useroot = True

if not roots:
    print("Cannot get roots of vocabulary")
    useroot = False

while True:
    word=str(input("Enter the word for sample sentence (empty for exit): "))
    if word == "":
        break
    try:
        print("Definition:", dic2[word])
        if not useroot:
            continue
        if roots[word]:
            print("Base means:", getbasemeaning(roots[word]))
    except KeyError:
        print("No definition and/or root found for \""+word+"\"\nPerhaps you misspelled it")
    try:
        pyperclip.copy(dic[word])
    except KeyError:
        print("No sample sentence found for \""+word+"\"\nPerhaps you misspelled it")
    else:
        print("(The sentence is copied to clipboard)")
