#   Version             Python 2.7
#   Author              Mathew Perrow
#   Description         Determining if branches in London and New York City
#                       are open using the current time at Portland HQ.
#
#
#
#

import datetime
import pytz

#   Define variable for current time in Portland
def find_time():
    dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
    dt_pdx = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
    hr_pdx = int(dt_pdx.strftime('%H'))     #Isolate the current hour time in Portland and change to integer
    hr_lon = (hr_pdx + 8)                   #Add 8 hours for London time zone difference
    hr_nyc = (hr_pdx + 3)                   #Add 3 hours for New York City time zone difference
    
    if (hr_nyc > 9) and (hr_nyc < 21):      #Branch is open if hr_nyc is between opening hours 9 and 21
        print('Yes the New York City branch is open.')
    else:
        print("I'm sorry the branch in New York City is not open.")

    if (hr_lon > 9) and(hr_lon < 21):       #Branch is open if hr_lon is between opening hours 9 and 21
        print('Yes the London branch is open.')
    else:
        print("I'm sorry the branch in London is not open.")


    


if __name__ =='__main__':
    find_time()
