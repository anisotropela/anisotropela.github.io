#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
import re
import datetime as dt
# import pandas

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

# Works only if sent on a Monday:
# deadline= dt.date.today()+dt.timedelta(days=2)
# nextDate= dt.date.today()+dt.timedelta(days=7)

# Works only if JC is *next* Monday:
# nextDate= next_weekday('Monday')
# deadline = nextDate + dt.timedelta(days=-5)

# data = pandas.read_xml('https://raw.githubusercontent.com/anisotropela/anisotropela.github.io/master/dawn/journal_club/moderators.xml')
# data = pandas.read_xml('./moderators.xml')
# 
# theModerator=" "
# theEmail=" "
# 
# for i in range(len(data["Date"])):
# 	if data["Date"][i]==nextDate.strftime('%m/%d/%Y'):
# 		theModerator = data["Moderator"][i]
# 		theEmail = data["Email"][i]

# Works if the date is correct in the moderators.xml file:
filename = 'moderators.xml'
with open(filename) as file:
    lines = [line.rstrip().lstrip() for line in file]

line1        = lines[1].split()
theDate      = re.findall('"([^"]*)"', line1[1])[0]
theModerator = re.findall('"([^"]*)"', line1[2])[0]
theEmail     = re.findall('"([^"]*)"', line1[3])[0]

nextDate = dt.datetime.strptime(theDate, '%Y/%m/%d')
deadline = nextDate + dt.timedelta(days=-5)

# override for testing purposes:
# theModerator="Peter L"
# theEmail = "pela@nbi.ku.dk"

email = """osascript -e 'tell application "Mail"
	
	set theFrom to ""
		set theTos to {" """ + theEmail + """ "}
		
		set theSubject to "Journal Club moderator reminder"
		set theDelay to 1
		set theContent to \"Dear """ + theModerator +""",\n\nThis is a reminder that it is your turn to moderate the next Journal Club session, i.e. Monday """ + nextDate.strftime('%d.%m') + """.\n\nThat means that you should\n\t0.  Respond to this message to avoid incessant reminders;\n\t1.  Pick two recent papers from the arXiv.org (you can find inspiration at benty-fields.com → Journal Club, if enough people have cast their votes);\n\t2.  Find two people that are willing to present them, preferably at the latest Wednesday """ + deadline.strftime('%d.%m')+""" and make them click the [Volunteer] button at Benty Fields; and\n\t3.  Send out a notification to the mailing list at Benty Fields (Journal Club  →  Members  →  ✉️Send group message).\n\nMore info at cosmicdawn.dk/wikidawn/dawn-activities/journal-club.\n\nNote: If you are not able to moderate this time, please find someone to swap with from the list on the website, and let me know.\n\n\nCheers,\nPeter.\"
		set theMessage to make new outgoing message with properties {sender:theFrom, subject:theSubject, content:theContent, visible:false}
		tell theMessage
			repeat with theTo in theTos
				make new recipient at end of to recipients with properties {address:theTo}
			end repeat
		end tell
		
		
		send theMessage
		
	end tell
	
	display notification "The Journal Club Reminder has been sent to the next moderator" with title "Moderator notified" sound name "Frog"'"""


# email = "osascript -e \'tell application \"Mail\"
# 	
# 	set theFrom to \"\"
# 		set theTos to {\" " + theEmail + " \"}
# 		
# 		set theSubject to \"Journal Club moderator reminder\"
# 		set theDelay to 1
# 		set theContent to \"Dear " + theModerator +",\n\nThis is a reminder that it is your turn to moderate the next Journal Club session, i.e. Monday " + nextDate.strftime('%d.%m') + ".\n\nThat means that you should\n\t0.  Respond to this message to avoid incessant reminders,\n\t1.  Pick two recent papers from the arXiv.org,\n\t2.  Find two people that are willing to present them, at the latest Wednesday " + deadline.strftime('%d.%m')+" and,\n\t3.  Send out a notification to the mailing list.\n\nSee more at cosmicdawn.dk/wikidawn/dawn-activities/journal-club, where you can also find an `auto-compose email` button and a list of possible presenters for inspiration.\n\nNote: If you are not able to moderate this time, please find someone to swap with from the list on the website, and let me know.\n\n\nCheers,\nPeter.\"
# 		set theMessage to make new outgoing message with properties {sender:theFrom, subject:theSubject, content:theContent, visible:false}
# 		tell theMessage
# 			repeat with theTo in theTos
# 				make new recipient at end of to recipients with properties {address:theTo}
# 			end repeat
# 		end tell
# 		
# 		
# 		send theMessage
# 		
# 	end tell
# 	
# 	display notification \"The Journal Club Reminder has been sent to the next moderator\" with title \"Moderator notified\" sound name \"Frog\"\'"
# 

print(email)

os.system(email)
