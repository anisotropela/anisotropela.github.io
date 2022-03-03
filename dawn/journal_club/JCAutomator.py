#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
import pandas
import datetime as dt

def next_weekday(weekday, d=dt.date.today()):
    """
    https://stackoverflow.com/questions/6558535/find-the-date-for-the-first-monday-after-a-given-a-date
    """
    if type(weekday) == str:
        weekday = weekday.lower()[:3]
        weekdays = ['mon','tue','wed','thu','fri','sat','sun']
        weekday  = weekdays.index(weekday)

    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + dt.timedelta(days_ahead)
#------------------------------------------------------------------------------



# deadline= dt.date.today()+dt.timedelta(days=2)
# nextDate= dt.date.today()+dt.timedelta(days=7)

nextDate= next_weekday('Monday')
deadline = nextDate + dt.timedelta(days=-5)


data = pandas.read_xml('https://www.anisotropela.dk/dawn/journal_club/moderators.xml')


theModerator=" "
theEmail=" "

for i in range(len(data["Date"])):
	if data["Date"][i]==nextDate.strftime('%m/%d/%Y'):
		theModerator = data["Moderator"][i]
		theEmail = data["Email"][i]


print(theEmail)
print(theModerator)

theModerator="Peter J"
theEmail = "peter.johannsen@nbi.ku.dk"



email = """osascript -e 'tell application "Mail"
	
	set theFrom to ""
		set theTos to {" """ + theEmail + """ "}
		
		set theSubject to "Journal Club moderator reminder"
		set theDelay to 1
		set theContent to \"Dear """ + theModerator +""",\n\nThis is a reminder that it is your turn to moderate the next Journal Club session, i.e. Monday """ + nextDate.strftime('%d.%m') + """. You should let the [resenters know by Wednesday """ + deadline.strftime('%d/%m')+""".\n\n Kind Regards, \n The Journal Club Team\"
		set theMessage to make new outgoing message with properties {sender:theFrom, subject:theSubject, content:theContent, visible:false}
		tell theMessage
			repeat with theTo in theTos
				make new recipient at end of to recipients with properties {address:theTo}
			end repeat
		end tell
		
		
		send theMessage
		
	end tell
	
	display notification "The Journal Club Reminder has been sent to the next moderator" with title "Moderator notified" sound name "Frog"'"""

print(email)

os.system(email)
