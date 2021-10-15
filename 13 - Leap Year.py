



def checkYear(givenYear):
    
    # The year has to be EVENLY divided by 4
    # By finding the remainder after dividing by 4
    # I can check if the remainder is equal to 0
    # If yes, then that means that is even.
    if (givenYear % 4) == 0:
        # print("YES, leap year.")

        if (givenYear % 100) == 0:

            if (givenYear % 400) == 0:
                print(str(givenYear) + " is a LEAP YEAR!\n")
        else: 
            print(str(givenYear) + " is a LEAP YEAR!\n")

    else:
        print(str(givenYear) +  " is NOT a leap year.")
        # print("Reason: not divisible by 4\n")


givenYear = int(input("Enter year: "))

checkYear(givenYear)