##region Assignment Information
# File: SentenceBuilder_Bullin.py
# Author: Jacob Emory Bullin
# Generates a sentence from words in a file, then display it
##endregion

##region Imports
import random
import pickle
##endregion

##region New Code
def writeFiles():
    fNames = ["nouns.txt", "verbs.txt", "articles.txt", "prepositions.txt"]
    for i in range(0, len(fNames)):
        pckl = open(fNames[i], "wb")
        print("Writing respons information for", fNames[i])
        r = []
        if (fNames[i] == "nouns.txt"):
            r = ["BOY",
                 "GIRL",
                "BAT",
                "BALL"]
        elif (fNames[i] == "verbs.txt"):
            r = ["HIT",
                 "SAW",
                 "LIKED"]
        elif (fNames[i] == "articles.txt"):
            r = ["A",
                 "THE"]
        elif (fNames[i] == "prepositions.txt"):
            r = ["WITH",
                 "BY"]
        for e in r:
            pickle.dump(e, pckl)
    pckl.close()

def getWords():
    fNames = ["nouns.txt", "verbs.txt", "articles.txt", "prepositions.txt"]
    n = []
    v = []
    a = []
    p = []
    words = [n, v, a, p]
    for i in range(0, len(fNames)):
        try:
            pckl = open(fNames[i], "rb")
            # print("Loaded Responses for", fNames[i])
            while True:
                try:
                    words[i].append(pickle.load(pckl))
                except (EOFError):
                    # print("File Load Failure")
                    break
        except IOError:
            writeFiles()
        pckl.close()
    return words

def main():
    writeFiles()
    w = getWords()
    nouns = tuple(w[0])
    verbs = tuple(w[1])
    articles = tuple(w[2])
    prepositions = tuple(w[3])
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence(nouns, verbs, articles, prepositions))


##endregion

##region Original Code
def sentence(nouns, verbs, articles, prepositions):
    return nounPhrase(nouns, verbs, articles, prepositions) + " " + verbPhrase(nouns, verbs, articles, prepositions)

def nounPhrase(nouns, verbs, articles, prepositions):
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase(nouns, verbs, articles, prepositions):
    return random.choice(verbs) + " " + nounPhrase(nouns, verbs, articles, prepositions) + " " + prepositionalPhrase(
        nouns, verbs, articles, prepositions)

def prepositionalPhrase(nouns, verbs, articles, prepositions):
    return random.choice(prepositions) + " " + nounPhrase(nouns, verbs, articles, prepositions)

if __name__ == "__main__":
    main()

##endregion
