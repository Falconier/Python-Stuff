##region Assignment Information
# Jacob Emory Bullin
# 2/28/19
# Conducts an interactive session of nondirective psychotherapy.
##endregion

##region Imports
import random
import pickle
from datetime import datetime
import itertools
##endregion

##region Questions
hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")
qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")
replacements = {"I": "you", "me": "you", "my": "your",
                "we": "you", "us": "you", "mine": "yours"}
##endregion

##region Original Code
def changePerson(sentence):


    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)
##endregion

##region New Code

def compare(s):
    rtn = False
    for e,f in itertools.combinations(s,2):
        if(e == f):
            rtn = True
            break

    return rtn

##endregion

##region Modified Code
def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    patient = input("Patient Name :> ")
    conversationP = []
    conversationT = []
    conversationT.append("What can I do for you?")
    count = 0
    percentage_chance = .25
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        conversationP.append(sentence)
        # compare the values in the list
        d = compare(conversationP)
        if(d):
            print("I am referring you to a specialist.")
            break
        r = random.randint(0,len(conversationP)-1)
        if(count >= 5 and random.random() < percentage_chance):
            response = reply(conversationP[r],True)
        else:
            response = reply(sentence,False)
        conversationT.append(response)
        print(response)

        count += 1

def reply(sentence,e):

    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if(e):
        return "Earlier you said that " + sentence
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)


##endregion


# The entry point for program execution
if __name__ == "__main__":
    main()
