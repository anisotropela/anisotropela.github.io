import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta

def next_weekday(weekday, d=datetime.date.today()):
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
    return d + timedelta(days_ahead)
#------------------------------------------------------------------------------

def list_days(day0=datetime.date.today(),ndays=10):
    """
    List every 7th day, starting with `day0`

    >>> list_days(datetime.date(2020,9,28))
    >>> next_monday = next_weekday(datetime.date.today(), 0)
    >>> list_days(next_monday)
    """
    if type(day0) == str:
        from dateutil import parser
        day0 = parser.parse(day0) # hackety-hack, better to use datetime.datetime.strptime('28 Oct 2020', '%d %b %Y'), but this needs the year

    dt    = timedelta(weeks=1)
    date  = day0
    dates = []

    dates.append(date.strftime('%Y/%m/%d'))
    for nday in range(ndays):
        date = date + dt
        dates.append(date.strftime('%Y/%m/%d'))

    return dates
#------------------------------------------------------------------------------

def n_participants():
    n = np.array([20 ,18 ,18 ,19 ,21 ,17 ,25 ,18 , 0 ,14 ,17 ,17])
    d = range(len(n))
    N = 25
    labels = ['28 Sep' ,'05 Oct' ,'12 Oct' ,'19 Oct' ,'26 Oct' ,'02 Nov' ,'09 Nov' ,'16 Nov' ,'23 Nov' ,'30 Nov' ,'07 Dec' ,'14 Dec']

    plt.clf()
    plt.bar(d,n/N*100,color='#0089C4')
    plt.xticks(d,labels,rotation=45,ha='right')
    plt.xlabel('Date')
    plt.ylabel('Participant percentage')
#------------------------------------------------------------------------------

def history(date       = '24 December',
            moderator  = 'DAWNer 0',
            presenter1 = 'DAWNer 1',
            arxiv1     = '1111.1111',
            title1     = 'Galaxies are awesome',
            author1    = 'Author 1',
            presenter2 = 'DAWNer 2',
            arxiv2     = '2222.2222',
            title2     = 'Lyman α is fun',
            author2    = 'Author 2'
            ):
    print('<h4>' + date + '</h4>')
    print('<ul>')
    print(' 	<li><b>' + presenter1 + '</b>: <a href="https://arxiv.org/abs/' + arxiv1 + '" target="_blank" rel="noopener">' + title1 + '</a> (' + author1 + ' et al.' + ')</li>')
    print(' 	<li><b>' + presenter2 + '</b>: <a href="https://arxiv.org/abs/' + arxiv2 + '" target="_blank" rel="noopener">' + title2 + '</a> (' + author2 + ' et al.' + ')</li>')
    print(' 	<li>Moderator: ' + moderator + '</li>')
    print('</ul>')
    print()
    print('<hr />')
#------------------------------------------------------------------------------
