##Filename: MorseCode.py
##Author: Jacob Emory Bullin
##Date:1-30-19

def main():
    De_Or_En = input("Do you want to decode or encode a message? (D/E):> ")
    if (De_Or_En == 'd' or De_Or_En == 'D'):
        theMessage = input("What message do you want to decode? \n:> ")
        # startTime = datetime.datetime.now()
        finalMsg = decode(theMessage)
        print("Decoded Message =>", finalMsg)
        # endTime = datetime.datetime.now()
        # elapsedTime = endTime - startTime
    else:
        theMessage = str(input("What message do you want to encode?\n:> "))
        finalMsg = encode(theMessage)
        print("Encoded Message =>", finalMsg)


def encode(msg):
    finMsg = ""
    msg = msg.lower()
    for i in range(len(msg)):
        ##Letter_to_Morse
        if (ord(msg[i]) == ord("a")):
            finMsg += ".-"
        elif (ord(msg[i]) == ord("b")):
            finMsg += "-..."
        elif (ord(msg[i]) == ord("c")):
            finMsg += "-.-."
        elif (ord(msg[i]) == ord("d")):
            finMsg += "-.."
        elif (ord(msg[i]) == ord("e")):
            finMsg += "."
        elif (ord(msg[i]) == ord("f")):
            finMsg += "..-."
        elif (ord(msg[i]) == ord("g")):
            finMsg += "--."
        elif (ord(msg[i]) == ord("h")):
            finMsg += "...."
        elif(ord(msg[i]) == ord("i")):
            finMsg += ".."
        elif(ord(msg[i]) == ord("j")):
            finMsg += ".---"
        elif(ord(msg[i]) == ord("k")):
            finMsg += "-.-"
        elif(ord(msg[i]) == ord("l")):
            finMsg += ".-.."
        elif(ord(msg[i]) == ord("m")):
            finMsg += "--"
        elif(ord(msg[i]) == ord("n")):
            finMsg += "-."
        elif(ord(msg[i]) == ord("o")):
            finMsg += "---"
        elif(ord(msg[i]) == ord("p")):
            finMsg += ".--."
        elif(ord(msg[i]) == ord("q")):
            finMsg += "--.-"
        elif(ord(msg[i]) == ord("r")):
            finMsg += ".-."
        elif(ord(msg[i]) == ord("s")):
            finMsg += "..."
        elif(ord(msg[i]) == ord("t")):
            finMsg += "-"
        elif(ord(msg[i]) == ord("u")):
            finMsg += "..-"
        elif(ord(msg[i]) == ord("v")):
            finMsg += "...-"
        elif(ord(msg[i]) == ord("w")):
            finMsg += ".--"
        elif(ord(msg[i]) == ord("x")):
            finMsg +="-..-"
        elif(ord(msg[i]) == ord("y")):
            finMsg +="-.--"
        elif(ord(msg[i]) == ord("z")):
            finMsg +="--.."
        elif(ord(msg[i]) == ord("1")):
            finMsg +=".----"
        elif (ord(msg[i]) == ord("2")):
            finMsg += "..---"
        elif (ord(msg[i]) == ord("3")):
            finMsg += "...--"
        elif (ord(msg[i]) == ord("4")):
            finMsg += "....-"
        elif (ord(msg[i]) == ord("5")):
            finMsg += "....."
        elif (ord(msg[i]) == ord("6")):
            finMsg += "-...."
        elif (ord(msg[i]) == ord("7")):
            finMsg += "--..."
        elif (ord(msg[i]) == ord("8")):
            finMsg += "---.."
        elif (ord(msg[i]) == ord("9")):
            finMsg += "----."
        elif (ord(msg[i]) == ord("0")):
            finMsg += "-----"
        else:
            finMsg += msg[i]

        finMsg += " "
    return finMsg

def decode(msg):
    if(msg[len(msg)-1] != " "):
        msg += ' '

    finMsg = ""
    charSet = ""
    for i in range(len(msg)):
        if(ord(msg[i]) == ord('.')):
            charSet += "."
        elif(ord(msg[i]) == ord('-')):
            charSet += "-"
        else:
            if(ord(msg[i]) == ord(' ')):
                ##Morse_to_Letter
                if(charSet == ".-"):
                    finMsg += 'a'
                elif(charSet == "-..."):
                    finMsg += 'b'
                elif(charSet == "-.-."):
                    finMsg += 'c'
                elif(charSet == "-.."):
                    finMsg += 'd'
                elif(charSet == "."):
                    finMsg += 'e'
                elif(charSet == "..-."):
                    finMsg += 'f'
                elif(charSet == "--."):
                    finMsg += 'g'
                elif(charSet == "...."):
                    finMsg += 'h'
                elif(charSet == ".."):
                    finMsg += 'i'
                elif(charSet == ".---"):
                    finMsg += 'j'
                elif(charSet == "-.-"):
                    finMsg += 'k'
                elif(charSet == ".-.."):
                    finMsg += 'l'
                elif(charSet == "--"):
                    finMsg += 'm'
                elif(charSet == "-."):
                    finMsg += 'n'
                elif(charSet == "---"):
                    finMsg += 'o'
                elif(charSet == ".--."):
                    finMsg += 'p'
                elif(charSet == "--.-"):
                    finMsg += 'q'
                elif(charSet == ".-."):
                    finMsg += 'r'
                elif(charSet == "..."):
                    finMsg += 's'
                elif(charSet == "-"):
                    finMsg += 't'
                elif(charSet == "..-"):
                    finMsg += 'u'
                elif(charSet == "...-"):
                    finMsg += 'v'
                elif(charSet == ".--"):
                    finMsg += 'w'
                elif(charSet == "-..-"):
                    finMsg += 'x'
                elif(charSet == "-.--"):
                    finMsg += 'y'
                elif(charSet == "--.."):
                    finMsg += 'z'

            try:
                if(ord(msg[i]) == ord(' ') and ord(msg[i+1]) == ord(' ') and ord(msg[i+2]) == ord(' ')):
                    finMsg += ' '
            except:
                continue

            charSet = ""

    return finMsg

main()