#Python:    2.7.13
#
#Author:    Mathew Perrow
#
#Purpose:   36 of 68 DRILLS -   This program will take the user through the process of cooking meat and dividing the meat amung
#                               dinner guests
#
#


import math



#Cooking meat in an oven until meat is to temp
def start():
    begin_cook()
    

def begin_cook():
    weight =raw_input('How many pounds of meat are you cooking?: ') #User inputs the weight of the meat he/she is cooking
    weight= my_int(weight)
    if not weight:
        begin_cook()
    print ('\nLets get {}lb of meat cooked for you.'.format(weight))
    cook_meat(weight)
   
    

def cook_meat(weight,time=0):         #determine how long to cook meat using lb of meat
    if time ==0:
        time = 15+(weight*5)    #time is in minutes
        print ('To cook {}lb of meat you must cook for {} minutes at temp of 375 Farenheit'.format(weight,time))
        print ('\nAfter cooking take out of oven and grab a thermometer.')
    check_meat(weight)
    return time
        

def check_meat(weight):  #Checking the temperature of the meat and determining if it needs more time
    print('\nPlace thermometer in center of meat and wait for temp to show')
    cooked = raw_input('\nWhat is the thermometer reading:') #inputting current temprature of meat
    cooked = my_int(cooked)
    if not cooked:
        check_meat(weight)
    if cooked<185:                      #If meat is less than 185 degrees it needs more time to cook
        moretime = (185-cooked)//3                          #moretime is in minutes
        print('Place back into oven and cook for {} minutes.'.format(moretime))
        check_meat(weight)
    else:
        print ('\nYour meat is done! Take out of oven and place on cooling rack')
        prepare_meat(weight)
        
        
def prepare_meat(weight):  #Asking user how many people will be eating and determining how much there will be in leftovers
    people = raw_input('How many people do you plan to serve meat to?')
    people = my_int(people)
    if not people:
        prepare_meat(weight)
    permeal = float(weight//people)
    leftover = float(weight - (permeal*people))
    print('There will be {}lb of meat for each person and {}lb of leftovers.'.format(permeal,leftover))
    print('\nEnjoy your meal!')
    
    

def my_int(num):            #Making sure input is an integer, pass num
    try:
        num=int(num)        #Change var to integer
        if num==0: raise Exception
    except:  #If input is string print 'bad input'
        print('bad input')
        return False
    return num





if __name__== '__main__':
    start()
    


