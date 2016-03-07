'''
Created on Mar 4, 2016

@author: Won_Lee
'''

import send_email
import view_calendar
import datetime


_MONTHS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
    }

def run_interface():
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    print()
    print('Welcome to the email reminder program!')
    print('   This program will assist you in')
    print('   creating an event and sending you')
    print('   an reminder email to your adress.')
    print()
    print()
    view_calendar.view(month, year=year)
    print()
    command = input('Do you want to choose a different year/month? (Yes/No): ')
    while command.lower() not in ['yes', 'no']:
        print(" input unrecognized; please enter 'yes' or 'no'")
        command = input('Do you want to choose a different year/month? (Yes/No)')
        print()
    if command.lower() == 'yes':
        year = input('  Which year? ')
        while type(eval(year)) != int:
            print('    Year must be an integer')
            year = input('  Which year? ')
        year = int(year)
        month = input('  Which month? (enter an integer): ')
        while ((type(eval(month)) != int) or ((int(month) < 0) or (int(month) > 12))):
            print('    Month must be an integer between 1 and 12, inclusively')
            month = input('  Which month? (enter an integer): ')
        month = int(month)
        #=======================================================================
        # print()
        # print(month, type(month), int(month), 1 <= int(month) <= 12)
        #=======================================================================
        view_calendar.view(month, year)

    print()
    print('''\
Schedule of your event:
   Year: {year}
   Month: {month}
   Day: Not Specified
   Name: Not Specified
'''.format(
    year = year,
    month = _MONTHS[month]))
    day = input('Please enter the day of your event: ')
    while (type(eval(day)) != int ) or ((int(day) < 0) or (int(day) > 31)):
        print('  Day must be an integer between 1 and 31, inclusively')
        day = input('Please enter the date of your event: ')
    name = input('Please enter the name of your event: ')
    print()
    print('''\
Schedule of your event:
   Year: {year}
   Month: {month}
   Day: {day}
   Name: {name}
'''.format(
    year = year,
    month = _MONTHS[month],
    day = day,
    name = name))
    print()
#===============================================================================
#     print('''\
# Year: {} {}
# MontH: {} {}
# Day: {} {}
# '''.format(year, type(year), month, type(month), day, type(day)))
#===============================================================================
    date = datetime.date(year, month, int(day))
    
    message = '''\

{name} on {month} {day}, {day_name}

Schedule of your event:
   Year: {year}
   Month: {month}
   Day: {day}
   Name: {name}
   
   
---------------------
this email was sent automatically through a program;
for questions and inquiries, please email jeromelee95@gmail.com

'''.format(
    year = year,
    month = _MONTHS[month],
    day = day,
    day_name = {0: 'Sunday', 1:'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}[date.weekday()],
    name = name)
    
    #===========================================================================
    # _want_changes = input('Do you want any changes? (Yes/No): ')
    # if _want_changes:
    #     
    #===========================================================================
    

    
    print('''\
Awesome! You have finished creating an event.
I will email these information so you won't forget.
Please enter your email address below:
''')
    while True:
        try:
            recipient_address = input('  Enter your email address (eg. example@example.com): ')
            print()
            print('sending your email.....')
            print()
            send_email.send(recipient_address, 'Your Scheduled Event!', message)
        except:
            print('unsuccessful; please enter your email again')
        else:

            break
        
        
    
    
    
if __name__ == '__main__':
    run_interface()
    
        

        