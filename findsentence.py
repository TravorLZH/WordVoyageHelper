import json
import pyperclip

inp=open("sentences.json")
content=inp.read()
inp.close()
while True:
    word=str(input("Enter the word for sample sentence (empty for exit): "))
    if word=="":
        break
    dic=json.loads(content)
    try:
        pyperclip.copy(dic[word])
    except KeyError:
        print("No sentence found for \""+word+"\"\nDid you misspelled it?")
    else:
        print("The sentence is copied to clipboard")
