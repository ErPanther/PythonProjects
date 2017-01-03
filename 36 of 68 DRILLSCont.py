#Python:    2.7.13
#
#Author:    Mathew Perrow
#
#Purpose:   36 of 68 DRILLS
#           Demonstrate while and for loops
#           and use of operators and operands
#          
#
#

numbers=(1,2,3,4,5,6,1,4,7,2)
itch={'Still Itches':True,'Still scratching':True,'Almost got it':True,'Releif':False} 

def start(itch): 
    for itches in itch:                             #go through itch dictionary
        print('Scratch your itch') 
        print itches                                #print first index in itch
    else:                                           #if itch is not true then print the following statement
        print('your itch not longer itches').capitalize() #loop is over itch has been releived
        print('now stop scratching you fiend!').capitalize()
        xtra(counter)




counter = 10
def xtra(counter):                                  #passing parameter counter into function xtra
    print ('your number will begin with %s') % counter
    while counter < 100:                            #Only begin block of instructions if counter is less than 100
        print('Do another iteration \nNumber is now %s') % counter
        while counter < 50:                         #nestled while statement if counter is larger than 50
            print('Do another one \nNumber is now %s') % counter
            counter += 10                           #Only do if counter is less than 50
        counter = (counter/12)*15                   #Calculation for counter if it is less than 100 and more than 50
    print('Your final number is now %s') % counter  #Show user what final counter value is
    usingforloop(numbers)

def usingforloop(numbers):                          #Finding numbers in a tuple
    for number in numbers:
        if number is 4:                             #If number is 4 print
            print ('This number is 4!')
        elif number is 7:
            print ('There is a 7 here')
        else:                                       #If number is neither 4 or 7 print
            print("There are other numbers here")


        

if __name__== '__main__':
    start(itch)
