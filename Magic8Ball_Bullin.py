import random, pickle

def main():
    responses = loadResponses()
    magicBall(responses)

def loadResponses():
    respns = []
    try:
        pckl = open("Magic8BallResponses_Bullin.data", "rb")
        print("Loaded Responses")
        while True:
            try:
                respns.append(pickle.load(pckl))
            except (EOFError):
                # print("File Load Failure")
                break
    except IOError:
        pckl = open("Magic8BallResponses_Bullin.data","wb")
        print("Writing Responses")
        r = ["Yes, of course!",
             "Without a doubt, yes.",
             "You can count on it.",
             "For sure!",
             "Ask me later.",
             "I\'m not sure.",
             "I can\'t tell you right now.",
             "I\'ll tell you after my nap.",
             "No way!",
             "I don\'t think so.",
             "Without a doubt , no.",
             "The answer is clearly NO"]
        for e in r:
            pickle.dump(e,pckl)
        loadResponses()
    pckl.close()
    return respns

def magicBall(r):
    while(True):
        question = input("Ask away (enter \'stop\' to exit): ")
        if(question.lstrip().rstrip().lower() == "stop"):
            break
        else:
            print(r[random.randint(0,11)])
    print("Terminated")

main()