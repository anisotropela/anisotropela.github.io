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

filename = 'moderators.xml' # used to be *moderators*, but now it's actually *presenters*
with open(filename) as file:
    lines = [line.rstrip().lstrip() for line in file]

line1        = lines[1].split() #\
line2        = lines[2].split() # \_ first four lines, containing the first four people (because line 0 is "<root>"
line3        = lines[3].split() # /
line4        = lines[4].split() #/

date1        = re.findall('"([^"]*)"', line1[1])[0] # Next Monday
date2        = re.findall('"([^"]*)"', line2[1])[0] # Next Monday
date3        = re.findall('"([^"]*)"', line3[1])[0] # The Monday after the next
date4        = re.findall('"([^"]*)"', line4[1])[0] # The Monday after the next

assert date1==date2, "The dates of presenters 1 and 2 are not the same " + "('" + date1 + "' and '" + date2 + "')."
assert date3==date4, "The dates of presenters 3 and 4 are not the same " + "('" + date3 + "' and '" + date4 + "')."

name1 = re.findall('"([^"]*)"', line1[2])[0] # First presenter in ~one week (if you send this a week before)
name2 = re.findall('"([^"]*)"', line2[2])[0] # Second -"-
name3 = re.findall('"([^"]*)"', line3[2])[0] # First presenter in ~two weeks
name4 = re.findall('"([^"]*)"', line4[2])[0] # Second -"-

email1     = re.findall('"([^"]*)"', line1[3])[0] #\
email2     = re.findall('"([^"]*)"', line2[3])[0] # \_corresponding emails
email3     = re.findall('"([^"]*)"', line3[3])[0] # /
email4     = re.findall('"([^"]*)"', line4[3])[0] #/

nextMonday = dt.datetime.strptime(date1, '%Y/%m/%d')         # next JC
theMondayAfterThat = dt.datetime.strptime(date3, '%Y/%m/%d') # next-next JC
deadline = nextMonday + dt.timedelta(days=-3)                # Friday before the next JC

test = False # Set to True to override names and emails (for testing purposes)
if test:
    name1="Peter"
    name2="Pede"
    name3="pela"
    name4="anisotropela"
    email1 = "pela@nbi.ku.dk"
    email2 = "darkpela@gmail.com"
    email3 = "pela@astro.uio.no"
    email4 = "anisotropela@gmail.com"

email = """osascript -e "tell application \\"Mail\\"

        set theFrom to \\"\\"
                set theTos to {{\\"{email1}\\", \\"{email2}\\"}}
                set theCcs to {{\\"{email3}\\", \\"{email4}\\"}}

                set theSubject to \\"Journal Club presentation reminder for {nextMonday}\\"
                set theDelay to 1
                set theContent to \\"
Dear {name1} and {name2} (cc. {name3} and {name4}; see PS in the bottom),

Here's a friendly reminder that you guys are up next for presenting a paper at the DAWN Journal Club, i.e. on Monday {nextMonday}.

This means that you should
    0.  Respond to this message NOW to avoid incessant reminders,
    1.  Pick a recent paper from the arXiv.org (you can find inspiration at benty-fields.com → DAWN Journal Club, if enough people have cast their votes),
    2.  Get back to me with the info at the latest Friday {deadline} (before I leave work), preferably in the following format:
        • FirstAuthor
        • Title
        • arXiv abstract link

More info at cosmicdawn.dk/wikidawn/dawn-activities/journal-club.

Note: If for any reason you are not able to present this time, please reach out to some of the next ones on the list:
cosmicdawn.dk/wikidawn/dawn-activities/journal-club#list-of-presenters,
and let me know once you've found someone to swap with. Note though that you can present remotely, if you like.


Cheers,
Peter

PS: {name3} and {name4}, this is also a notification for you that you're next in line, i.e. on Monday {theMondayAfterThat}. You will get a second reminder next Monday :)\\"
                set theMessage to make new outgoing message with properties {{sender:theFrom, subject:theSubject, content:theContent, visible:false}}
                tell theMessage
                        repeat with theTo in theTos
                                make new recipient at end of to recipients with properties {{address:theTo}}
                        end repeat
                        repeat with theCc in theCcs
                                make new cc recipient at end of cc recipients with properties {{address:theCc}}
                        end repeat
                end tell

                send theMessage

        end tell

        display notification \\"The Journal Club Reminder has been sent to the next presenters\\" with title \\"Presenters notified\\" sound name \\"Frog\\"" """.format(
    email1=email1,
    email2=email2,
    email3=email3,
    email4=email4,
    name1=name1,
    name2=name2,
    name3=name3,
    name4=name4,
    nextMonday=nextMonday.strftime('%d.%m'),
    theMondayAfterThat=theMondayAfterThat.strftime('%d.%m'),
    deadline=deadline.strftime('%d.%m')
)

print(email)

os.system(email)
