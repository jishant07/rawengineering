"""
NOTE : This is a CLI interface mimicing a POS transaction system
DEPENDENCIES : This code is run and debugged on Python 3.8
"""

print("------------------------MANAGER SIDE------------------------")
print("Let's start with the total money you have with you")

#TAKING INPUT FROM MANAGER 
total = int(input("Enter the total amount you have: "))

#NOTE : ASSUMED TO HAVE DENOMINATIONS IN FORM OF 2000s, 500s, 100s, 50s and 10s CURRENCY NOTES AND 1 RUPEE COIN
avail = {2000:0,500:0,100:0,50:0,10:0,1:0}
initAvail = avail
print(" ")
print("NOTE : Add denominations of that you are having the amount in")
def denomcheck(avail,total):
    sum = 0
    print(" ")
    print("------------------------DENOMINATION CHECK------------------------")
    #cross checking denom total and actual total
    while sum != total:     
        print("1. Add number of 2000 notes")
        print("2. Add number of 500 notes")
        print("3. Add number of 100 notes")
        print("4. Add number of 50 notes")
        print("5. Add number of 10 notes")
        print("6. Add number of 1 coins")
        print("7. Exit")
        print(" ")
        ch = int(input("Enter your choice: "))
        print(" ")
        if(ch > 7 or ch < 1):
            print("ERROR : Invalid input")
        elif(ch == 1):
            num = int(input("Enter Number of 2000s notes: "))
            if(avail[2000] != 0):
                avail[2000] = avail[2000] + num
            else:
                avail[2000] = num
            sum  = sum + (2000 * num)
        elif(ch == 2):
            num = int(input("Enter Number of 500s notes: "))
            if(avail[500] != 0):
                avail[500] = avail[500] + num
            else:
                avail[500] = num
            sum  = sum + (500 * num)
        elif(ch == 3):
            num = int(input("Enter Number of 100s notes: "))
            if(avail[100] != 0):
                avail[100] = avail[100] + num
            else:
                avail[100] = num
            sum  = sum + (100 * num)
        elif(ch == 4):
            num = int(input("Enter Number of 50s notes: "))
            if(avail[50] != 0):
                avail[50] = avail[50] + num
            else:
                avail[50] = num
            sum  = sum + (50 * num)
        elif(ch == 5):
            num = int(input("Enter Number of 10s notes: "))
            if(avail[10] != 0):
                avail[10] = avail[10] + num
            else:
                avail[10] = num
            sum  = sum + (10 * num)
        elif(ch == 6):
            num = int(input("Enter Number of 1 Rupee coins: "))
            if(avail[1] != 0):
                avail[1] = avail[1] + num
            else:
                avail[1] = num
            sum  = sum + (1 * num)
        elif(ch == 7):
            print("Exiting ...")
            if(sum == total):
                print(avail)
                return True
            else:
                avail = initAvail
                sum = 0
                return False

    if sum != total:
        avail = initAvail
        sum = 0
        return False
    else:
        print(avail) 
        return True

if(denomcheck(avail,total)):
    initAvail = avail
    print(" ")
    print("------------------------TRANSACTION BEGINS------------------------")
    #Assuming integer bill amount as the currency is in integer
    billamount = int(input("Enter bill amount to be paid by the customer: ")) 
    paidWith = int(input("Enter the amount paid by the customer: "))

    #runs only if the amount paidWith is lesser than the billing amount
    while paidWith < billamount:    
        if(paidWith < billamount):
            print("ERROR : Not sufficient to pay the bill")

    print(" ")
    print("Note : Enter the denomination received from customer")

    if(denomcheck(avail,paidWith)):
        returnAmount = paidWith - billamount
        print("Return total amount of " + str(returnAmount) + " in form of following denominations")

        #Populating the available denomination that we can pay up with
        availDenoms = dict()    
        for (key,val) in avail.items():
            if(val>0 and key <= returnAmount):
                availDenoms[key] = val

        if(len(availDenoms.keys()) > 0):
            for (key,val) in availDenoms.items():
                if(returnAmount//key <= val):
                    tempNum = returnAmount//key
                    updateVal = val - tempNum
                    print("Number of notes of "+str(key)+"s x"+str(returnAmount//key))
                    returnAmount = returnAmount % key
                    availDenoms[key] = updateVal
                    if(returnAmount == 0):
                        break

            if(returnAmount > 0):
                print("ERROR : Transaction cannot be completed because needed denominations aren't available")

        else:
            print("ERROR : No denominations available to make payments")
    else:
        print("ERROR : The customer didn't pass the denom check")

else :
    print("ERROR : Didn't pass denomination check")
