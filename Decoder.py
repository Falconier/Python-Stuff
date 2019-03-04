## decoder group activity

import datetime
def main():
    De_Or_En = input("Do you want to decode or encode a message? (D/E):> ")
    if(De_Or_En == 'd' or De_Or_En == 'D'):
        theMessage = input("What message do you want to decode? \n:> ")
        # startTime = datetime.datetime.now()
        finalMsg, elapsedTime = decode(theMessage.lower)
        # endTime = datetime.datetime.now()
        # elapsedTime = endTime - startTime
        prntTime(elapsedTime)
    else:
        theMessage = input("What message do you want to encode?\n:> ")
        while True:
            shiftDistance = int(input("Shift Distance (Please enter a number between 1 and 25) :> "))
            if(shiftDistance >= 1 and shiftDistance <= 25):
                break
        finalMsg = encode(theMessage, shiftDistance)
        print("Encoded Message =>", finalMsg, "\nShifted by", shiftDistance, "characters.")

def decode(msg):
    startTime = datetime.datetime.now()

    distance = 1
    decodedMsg = ""

    while True:
        for ch in msg:
            ordvalue = ord(ch)
            ciphervalue = ordvalue - distance
            if ciphervalue < ord('a'):
                ciphervalue = ord('z') - (distance + (ord('a') - ordvalue - 1))
            decodedMsg += chr(ciphervalue)
        ans = input("Decode Message => " + str(decodedMsg) + "\nIs this correct? (Y/N) :> ")
        if(ans == 'Y' or ans == 'y'):
            endTime = datetime.datetime.now()
            time = endTime - startTime
            break
        else:
            distance += 1
            decodedMsg = ""
    return decodedMsg, time

def prntTime(time):
    print("Seconds:", time.seconds, ", MicroSeconds:", time.microseconds)

def encode(msg, dist):
    encodedMsg = ""
    dist = dist
    for ch in msg:
        ordvalue = ord(ch)
        ciphervalue = ordvalue + dist
        if ciphervalue > ord('z'):
            ciphervalue = ord('a') + dist - (ord('z') - ordvalue + 1)
        encodedMsg += chr(ciphervalue)
    return encodedMsg


main()