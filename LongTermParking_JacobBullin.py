## LongTermParking_JacobBullin.py
## calculate charge for long-term parking
## 1-31-19

import datetime
import pickle


def main():
    dateTimeInfo = input("When did you park? (enter date and time following the example Aug 12 2018  6:30AM) :> ")

    timeIn = datetime.datetime.strptime(dateTimeInfo, '%b %d %Y %I:%M%p')

    parkedTime,timeOut = calcTime(timeIn)

    print(parkedTime)
    fee = calcCharge(parkedTime)
    print("$" + fee)

    saveTicket(timeIn,timeOut,parkedTime,fee)

def calcTime(inDateTime):
    outDateTime = datetime.datetime.now()
    calcElapsedTime = outDateTime-inDateTime

    return calcElapsedTime,outDateTime

def calcCharge(elapsedTime):
    hours = elapsedTime.seconds/3600
    days = elapsedTime.days
    if(days >= 1):
        dayFee = days * 10

    if(hours >= 1 and hours <5):
        hourFee = hours * 2
    elif(hours >= 5):
        hourFee = 10

    totalFee = dayFee + hourFee
    totalFee = "%.2f" % totalFee

    return totalFee

def saveTicket(timeIn, timeOut, parkedTime, fee):
    todayDate = datetime.datetime.now().strftime("%b-%d-%y")
    fileName = "ParkingLog_" + todayDate + ".data"
    startPick = open(fileName,"wb")
    logEntry = "<Time In:", timeIn, "> <Time Out:", timeOut,"> <Time Parked:", parkedTime, "> <Fee (in Dollars):", fee,">"
    pickle.dump(logEntry, startPick)
    startPick.close()

main()