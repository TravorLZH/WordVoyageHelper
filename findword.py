import pyperclip
from getsentences import getsentences
from getdefinitions import getdefinitions


dic=getsentences()
dic2=getdefinitions()
while True:
    word=str(input("Enter the word for sample sentence (empty for exit): "))
    if word=="":
        break
    try:
        print(dic2[word])
    except KeyError:
        print("No definition found for \""+word+"\"\nPerhaps you misspelled it")
    try:
        pyperclip.copy(dic[word])
    except KeyError:
        print("No sample sentence found for \""+word+"\"\nPerhaps you misspelled it")
    else:
        print("(The sentence is copied to clipboard)")
