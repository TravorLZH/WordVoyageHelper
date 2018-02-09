import pyperclip
from getsentences import getsentences
from getdefinitions import getdefinitions
from getroots import getroots

dic = getsentences()
dic2 = getdefinitions()
roots=getroots()

while True:
    word=str(input("Enter the word for sample sentence (empty for exit): "))
    if word == "":
        break
    try:
        print("Definition:", dic2[word])
        if roots[word]:
            print("Roots:", roots[word])
    except KeyError:
        print("No definition found for \""+word+"\"\nPerhaps you misspelled it")
    try:
        pyperclip.copy(dic[word])
    except KeyError:
        print("No sample sentence found for \""+word+"\"\nPerhaps you misspelled it")
    else:
        print("(The sentence is copied to clipboard)")
