'''
Created on Jan 14, 2021

@author: jct

Utility function to create an RFC-822 compliant date string,
representing the current time, to use as the "Date:" field of an email
message.
'''

import datetime
from pytz import timezone
from email import utils

# See:
# https://stackoverflow.com/questions/7065164/how-to-make-an-unaware-datetime-timezone-aware-in-python?

def centraltime_str():
    # Get a datetime structure representing the current time
    nowdt = datetime.datetime.now()
    
    # Get the timezone object for Houston
    c = timezone('US/Central')

    # Make the current time object location-aware
    loc_dt = c.localize(nowdt)
    
    # Turn the datetime object into an RFC-822 compatible string...
    now_str = utils.format_datetime(loc_dt)
    
    # ...and return it
    return now_str

if __name__ == '__main__':
    now_str = centraltime_str()
    print("Central Time String = <%s>" % now_str)
