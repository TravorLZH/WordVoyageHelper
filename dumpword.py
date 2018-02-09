from getdefinitions import getdefinitions
from getwords import getwords
from getsentences import getsentences
import csv

words = getwords()
sentences = getsentences()
definitions = getdefinitions()

with open("vocab.csv", "w") as output:
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Words', 'Definition', 'Sample Sentences'])
    for word in words:
        writer.writerow([word, definitions[word], sentences[word]])
