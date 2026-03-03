#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import requests
import datetime as dt
import xml.etree.ElementTree as ET
import time


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

zoom_link = "https://ucph-ku.zoom.us/j/64115008249?pwd=N2tBWjhPZ1pneUJVU016d2djU3Z4QT09"
#recipients = ["Pedefar <pela@nbi.ku.dk>"]   # <-- change to your mailing list
recipients = ["DAWN Journal Club <dawn_journalclub@nbi.ku.dk>"]   # <-- change to your mailing list


# ------------------------------------------------------------
# Time phrasing logic
# ------------------------------------------------------------

def get_time_phrase():
    now = dt.datetime.now()
    today = now.date()

    # Next Tuesday 13:00 (this week's if today <= Tuesday, otherwise next week)
    weekday_target = 1  # Tuesday (Monday=0)
    days_ahead = weekday_target - today.weekday()
    if days_ahead < 0:
        days_ahead += 7

    jc_date = today + dt.timedelta(days=days_ahead)
    jc_datetime = dt.datetime.combine(jc_date, dt.time(13, 0))

    delta = jc_datetime - now

    if today.weekday() < 0 or today.weekday() > 1:
        return "tomorrow at 13:00"

    if today.weekday() == 0:  # Monday
        return "Tuesday at 13:00"

    if today.weekday() == 1:  # Tuesday
        total_minutes = int(delta.total_seconds() // 60)

        if now.hour < 12:
            hours = total_minutes // 60
            minutes = total_minutes % 60
            return f"in {hours:02d}:{minutes:02d} hours"
        else:
            return f"in {total_minutes} minutes"

    return "tomorrow at 13:00"


# ------------------------------------------------------------
# arXiv metadata
# ------------------------------------------------------------

def fetch_arxiv(arxiv_id):
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    r = requests.get(url)

    if r.status_code != 200:
        raise RuntimeError(f"Error contacting arXiv API (status {r.status_code}).")

    root = ET.fromstring(r.text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    entry = root.find("atom:entry", ns)

    if entry is None:
        raise ValueError(f"Sorry, arXiv ID {arxiv_id} does not exist.")

    title_elem = entry.find("atom:title", ns)
    authors = entry.findall("atom:author/atom:name", ns)

    if title_elem is None or not authors:
        raise ValueError(f"Incomplete metadata returned for arXiv ID {arxiv_id}.")

    title = title_elem.text.strip().replace("\n", " ")
    author_list = [a.text for a in authors]

    first_author_lastname = author_list[0].split()[-1]

    if len(author_list) > 1:
        author_line = f"{first_author_lastname} et al."
    else:
        author_line = first_author_lastname

    return author_line, title


# ------------------------------------------------------------
# Email body construction
# ------------------------------------------------------------

def build_email(presenters, arxiv_ids):
    time_phrase = get_time_phrase()

    paper_word = "paper" if len(presenters) == 1 else "papers"

    intro = (
        f"Dear all,\n\n"
        f"Please join us for the DAWN Journal Club {time_phrase} "
        f"where we will be discussing the following {paper_word}:\n\n"
    )

    body = ""

    for name, arxiv_id in zip(presenters, arxiv_ids):
        author_line, title = fetch_arxiv(arxiv_id)
        url = f"https://arxiv.org/abs/{arxiv_id}"

        body += f"{name}:\n"
        body += f" - {author_line}\n"
        body += f" - {title}\n"
        body += f" - {url}\n\n"

    ending = (
        f"Zoom link: {zoom_link}\n\n\n"
        f"Cheers,\n"
        f"Peter"
    )

    return intro + body + ending


# ------------------------------------------------------------
# Send via Mail.app
# ------------------------------------------------------------

def send_email(subject, content):
    # Remove leading whitespace/newlines
    clean_content = content.lstrip()

    tos = ", ".join([f"\"{r}\"" for r in recipients])

    applescript = f"""osascript -e 'tell application "Mail"
        set theSubject to "{subject}"
        set theContent to "{clean_content.replace('"', '\\"')}"
        set theMessage to make new outgoing message with properties {{subject:theSubject, content:theContent, visible:false}}
        tell theMessage
            make new recipient at end of to recipients with properties {{address:{tos}}}
        end tell
        send theMessage
        return
    end tell'"""

    os.system(applescript)


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():
    args = sys.argv[1:]

    if len(args) not in [2, 4]:
        print("Usage:")
        print("  python send_jc.py Name arXivID [Name arXivID]")
        sys.exit(1)

    presenters = args[0::2]
    arxiv_ids = args[1::2]

    try:
        content = build_email(presenters, arxiv_ids)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    subject = "DAWN Journal Club"
    content = build_email(presenters, arxiv_ids)
    print()
    print("Sending the following:")
    print()
    print("-------------------------")
    print(content)
    print("-------------------------")
    print()
    for i in range(5, -1, -1):
        print(f"\rSending the email in {i} seconds", end="", flush=True)
        time.sleep(1)
    print()

    send_email(subject, content)


if __name__ == "__main__":
    main()
