'''
Created on Mar 4, 2016

@author: Won_Lee
'''

import calendar



def view(month, year = 2016):
    
    assert type(month) == int
    assert 1 <= int(month) <= 12
    
    try:
        c = calendar.TextCalendar(calendar.SUNDAY)
        c.prmonth(year, month)
        
    except:
        raise AssertionError
    
    