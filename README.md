# email_reminders

Assists in setting up a schedule and sends an auto-created email with corresponding information.

Download all files in the same folder the run the ' interface.py ' file to run the program. A text-based calender is displayed in python shell and asks the user to specify the year/month. After presenting the calendar, the user is asked to specify the exact day/name of the event. The program then asks for the user's email address then sends an auto-created email with corresponding information about the schedule.

Sample interaction:


```

Welcome to the email reminder program!
   This program will assist you in
   creating an event and sending you
   an reminder email to your adress.


     March 2016
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
 
Do you want to choose a different year/month? (Yes/No): no

Schedule of your event:
   Year: 2016
   Month: March
   Day: Not Specified
   Name: Not Specified

Please enter the day of your event: 8
Please enter the name of your event: Meeting with Board Members

Schedule of your event:
   Year: 2016
   Month: March
   Day: 8
   Name: Meeting with Board Members


Awesome! You have finished creating an event.
I will email these information so you won't forget.
Please enter your email address below:

  Enter your email address (eg. example@example.com): jeromelee95@gmail.com

sending your email.....

Email sent successfully

```

The recieved email will be sent from wonjoolee.testing@gmail.com and will be in this form:

```

Meeting with Board Members on March 8, Monday

Schedule of your event:
   Year: 2016
   Month: March
   Day: 8
   Name: Meeting with Board Members


---------------------
this email was sent automatically through a program;
for questions and inquiries, please email jeromelee95@gmail.com

```


