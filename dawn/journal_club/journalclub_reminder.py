#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import argparse
import re
import os
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

def n_to_ordinal(n):
    ordinals = ['zeroth',
                'first',
                'second',
                'third',
                'fourth',
                'fifth',
                'sixth',
                'seventh',
                'eighth',
                'ninth',
                'tenth']
    return ordinals[n]
#------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
            description='Send an email reminder to a notifee. Example of a second reminder:\n  $ python journalclub_reminder.py -e "Peter Laursen <pela@nbi.ku.dk>" -n 2',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-n', '--nth_reminder',
        type=int,
        help='Integer. This is the `nth_reminder` reminder')
    parser.add_argument(
        '-e', '--email',
        type=str,
        help='String. Notifee name and email address, e.g.\n'
             '"Ole Bole <olebole@skole.dk>"'
    )
    args = parser.parse_args()

    n     = args.nth_reminder
  # assert n >= 2, "The *notification* was the first reminder, so you should start with n = 2."
    if n < 2: # Cleaner exit than assertion error
        print("The *notification* was the first reminder, so you should start with n = 2.")
        exit()
    email_address = args.email
    try:
        name    = re.match("(.*?)<",email_address).group(1)
        address = re.search('<(.*)>',email_address).group(1)
    except:
        print('Name and email should be in the format "Ole Bole <olebole@skole.dk>", including quotes and </> signs.')

    nth   = n_to_ordinal(n)
    today = dt.date.today()

    next_monday = next_weekday('mon')
    next_monday = dt.datetime.strptime(str(next_monday), '%Y-%m-%d')
    deadline    = next_monday + dt.timedelta(days=-3)                # Friday before the next JC

    email_text = """osascript -e "tell application \\"Mail\\"

            set theFrom to \\"\\"
                    set theTo to {{\\"{address}\\"}}

                    set theSubject to \\"{nth} Journal Club presentation reminder for {next_monday}\\"
                    set theDelay to 1
                    set theContent to \\"
Dear {name},

This is the {nth} friendly reminder that you are up next for presenting a paper at the DAWN Journal Club on Monday {next_monday}.

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
Peter\\"
                    set theMessage to make new outgoing message with properties {{sender:theFrom, subject:theSubject, content:theContent, visible:false}}
                    tell theMessage
                            make new recipient at end of to recipients with properties {{address:theTo}}
                    end tell

                    send theMessage

            end tell

            display notification \\"The Journal Club Reminder has been sent to the next presenters\\" with title \\"Presenters notified\\" sound name \\"Frog\\"" """.format(
        address=address,
        name=name,
        nth=nth,
        next_monday=next_monday.strftime('%d.%m'),
        deadline=deadline.strftime('%d.%m')
    )

    print(email_text)

    os.system(email_text)

if __name__ == '__main__':
    main()
