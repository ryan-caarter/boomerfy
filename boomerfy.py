import random
import sys
from nltk.corpus import wordnet as wn

text = input("What's on your mind?: ")
text = text.split(" ")
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
adjectives = ["hairy", "sophisticated", "malnourished", "chinese", "sheep", "jabbing", "propaganda", "scamming", "gas", "worked", "psychotic", "medicated", "tread", "imprisoned", "media"]
result = ""
for word in text:
    if word in nouns:
        word = word.upper()
        if random.randint(0,1):
            variable = random.randint(0, len(adjectives))-1
            word = adjectives[variable] + " " + word
            adjectives = adjectives[:variable] + adjectives[variable+1:]
    result += word + " "

if random.randint(0,1) == 1:
    result += " PLEASE "

if random.randint(0,1) == 1:
    result += "!!!"

print(result)
