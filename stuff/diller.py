import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes

def dillit(language    = 'dk',
           html        = False,
           year_hist   = True,
           page_hist   = True,
           country_pie = True,
           stats       = True):
    """
    Landekoder følger FIFA: https://en.wikipedia.org/wiki/List_of_FIFA_country_codes
    """
    plt.close('all')
    #                0          1                                            2     3       4                                       5                                                  6     7    8     9    10    11    12                                                                                                                                                                                          Mi    Mo    Je    Kl    Pe
    books = [['2022.01.08', 'Lone Frank'                                 , 'DEN', 'F', 'Størst af alt'                      , 'Størst af alt'                                      , 2020, 292, nan , nan , nan , nan , nan],
             ['2021.10.29', 'Jack Kerouac'                               , 'USA', 'M', 'Vejene'                             , 'On the Road'                                        , 1957, 285, 2   , 3.5 , 4.5 , 3   , 1.5],
             ['2021.08.14', 'Giuseppe Tomasi di Lampedusa'               , 'ITA', 'M', 'Leoparden'                          , 'The Leopard'                                        , 1958, 247, 2   , 3.5 , 1.5 , 3   , 3.5],
          #  ['2021.08.14', 'Giuseppe Tomasi di Lampedusa'               , 'ITA', 'M', 'Leoparden'                          , 'The Leopard'                                        , 1958, 247, 2,5 , 3   , 2   , 2.5 , 4  ], # Kareten
             ['2021.06.12', 'William Golding'                            , 'ENG', 'M', 'Fluernes herre'                     , 'Lord of the Flies'                                  , 1954, 196, 3   , 1.5 , 4   , 3.5 , 3.5],
             ['2021.04.03', 'Ray Bradbury'                               , 'USA', 'M', 'Krøniker fra Mars'                  , 'The Martian Chronicles'                             , 1950, 192, nan , 4   , 2   , 3   , 4  ],
             ['2021.04.03', 'Alistair MacLean'                           , 'SCO', 'M', 'Ørneborgen'                         , 'Where Eagles Dare'                                  , 1967, 166, 2.5 , 3.5 , 4   , 2   , 2.5],
             ['2021.01.30', 'Vladimir Nabokov'                           , 'USA', 'M', 'Lolita'                             , 'Lolita'                                             , 1955, 307, 4.5 , 4   , 3.5 , 4   , 4.5],
             ['2020.11.21', 'Halldór Laxness'                            , 'ISL', 'M', 'Salka Valka'                        , 'Salka Valka'                                        , 1931, 373, 3   , 3   , 2   , 3   , 4  ],
             ['2020.09.18', 'Laurence Sterne'                            , 'ENG', 'M', 'Tristram Shandys levned og meninger', 'The Life and Opinions of Tristram Shandy, Gentleman', 1759, 588, 2   , 3   , 3   , 3.5 , 2  ],
             ['2020.05.30', 'José Saramago'                              , 'POR', 'M', 'En fortælling om blindhed'          , 'Blindness'                                          , 1995, 284, 4   , 4.5 , 3.5 , 4   , 4.5],
             ['2020.04.04', 'Iain M. Banks'                              , 'SCO', 'M', 'Hvepsefabrikken'                    , 'The Wasp Factory'                                   , 1984, 232, nan , nan , nan , nan , 4  ],
             ['          ', 'Arto Paasilinna'                            , 'FIN', 'M', 'Harens år'                          , 'The Year of the Hare'                               , 1975, 183, 3.5 , 3   , 5   , 2.5 , 3.5],
             ['          ', 'Siri Hustvedt'                              , 'USA', 'F', 'Den flammende verden'               , 'The Blazing World'                                  , 2014, 434, 3.5 , 4.5 , 3   , 4   , 4  ],
             ['          ', 'Isaac Asimov'                               , 'USA', 'M', 'Stålhulerne'                        , 'Caves of Steel'                                     , 1953, 214, 1.5 , 1.5 , 2   , 1.5 , 2  ],
             ['          ', 'Sophus Helle og Morten Søndergaard (overs.)', 'SUM', 'M', 'Gilgamesh'                          , 'Gilgamesh'                                          ,-2100, 140, 4   , 5   , 2.5 , 3.5 , 4  ],
             ['          ', 'Brett Easton Ellis'                         , 'USA', 'M', 'Under nul'                          , 'Less than zero'                                     , 1985, 163, 2.5 , 3   , 4   , 2.5 , 2  ],
             ['          ', 'F. Scott Fitzgerald'                        , 'USA', 'M', 'Den store Gatsby'                   , 'The Great Gatsby'                                   , 1925, 171, 2   , 1.5 , 4.5 , 2.5 , 2.5],
             ['          ', 'Günther Grass'                              , 'GER', 'M', 'Bliktrommen'                        , 'The Tin Drum'                                       , 1959, 555, 1   , 2   , 0   , 2   , 2.5],
             ['          ', 'Peter Adolphsen'                            , 'DEN', 'M', 'Rynkekneppesygen'                   , 'Rynkekneppesygen'                                   , 2017, 245, 3.5 , 3.5 , 3.5 , 3.5 , 4  ],
             ['          ', 'Svend Aage Madsen'                          , 'DEN', 'M', 'Mellem Himmel og Jord'              , 'Between Heaven and Earth'                           , 1990, 208, 4   , 4   , 4   , 4   , 4.5],
             ['          ', 'Os selv'                                    , 'DEN', 'M', 'Vi skrev vores egne noveller'       , 'We wrote our own short stories'                     , 2018,  18, 5   , 5   , nan , nan , 5  ],
             ['          ', 'Louis-Ferdinand Céline'                     , 'FRA', 'M', 'Død på kredit'                      , 'Death on Credit'                                    , 1936, 508, 5   , 5   , 5   , 5   , 4.5],
             ['          ', 'Karen Blixen'                               , 'DEN', 'F', 'Syv fantastiske fortællinger'       , 'Seven Gothic Tales'                                 , 1934, 500, 2   , 2.5 , 1   , 2.5 , 3.5],
             ['          ', 'Erich Maria Remarque'                       , 'GER', 'M', 'Intet nyt fra Vestfronten'          , 'All Quiet on the Western Front'                     , 1929, 202, 4   , 4.5 , 4.5 , 4.5 , 4  ],
             ['          ', 'Jens Blendstrup'                            , 'DEN', 'M', 'Slagterkoner og bagerenker'         , 'Slagterkoner og Bagerenker'                         , 2016, 418, 4.5 , 4   , 4.5 , 4   , 4  ],
             ['          ', 'Jan Sonnergaard'                            , 'DEN', 'M', 'Radiator'                           , 'Radiator'                                           , 1997, 221, 3.5 , 3   , 5   , 3.5 , 4  ],
             ['2017.02.10', 'H. P. Lovecraft'                            , 'USA', 'M', 'The Call of Cthulhu'                , 'The Call of Cthulhu; The Whisperer in the Darkness' , 1928, 117, 4.5 , 4.5 , 2   , 4.5 , 4.5],
             ['2016.11.19', 'John le Carré'                              , 'ENG', 'M', 'Spionen der kom ind fra kulden'     , 'The Spy Who Came in from the Cold'                  , 1963, 225, 2   , 2   , 2.5 , 2   , 2.5],
             ['2016.08.26', 'Peter Madsen'                               , 'DEN', 'M', 'Historien om Job'                   , 'The Book of Job (comic book version)'               , -450, 104, 1   , 1.5 , nan , nan , 0.5],
             ['2016.08.26', 'Virginia Woolf'                             , 'ENG', 'F', 'Til Fyret'                          , 'To the Lighthouse'                                  , 1927, 210, 2   , 2.5 , 2   , 3   , 3  ],
             ['          ', 'Aksel Sandemose'                            , 'DEN', 'M', 'En flygtning krydser sit spor'      , 'A Fugitive Crosses his Tracks'                      , 1933, 425, 4.5 , 4.5 , 2   , 4.5 , 4.5],
             ['          ', 'Morten Pape'                                , 'DEN', 'M', 'Planen'                             , 'Planen'                                             , 2015, 557, 4.5 , 4.5 , 4.5 , 3.5 , 4.5],
             ['          ', 'Orhan Pamuk'                                , 'TUR', 'M', 'Det hvide slot'                     , 'The White Castle'                                   , 1985, 160, 3.5 , 3.5 , nan , 3.5 , 4  ],
             ['          ', 'Thomas Pynchon'                             , 'USA', 'M', 'Det dybe net'                       , 'Bleeding Edge'                                      , 2013, 519, 0.5 , 0.5 , 0   , 0.5 , 0.5],
             ['2015.10.10', 'Dan Turèll'                                 , 'DEN', 'M', 'Vangede billeder'                   , 'Vangede Billeder'                                   , 1975, 193, 4   , 3.5 , 4   , 3   , 3.5],
             ['2015.08.28', 'Harper Lee'                                 , 'USA', 'F', 'Dræb ikke en sangfugl'              , 'To Kill a Mocking Bird'                             , 1960, 307, 3   , 3   , 3.5 , 3   , 3.5],
             ['2015.05.14', 'Michel Houellebecq'                         , 'FRA', 'M', 'Kortet og landskabet'               , 'The Map and the Territory'                          , 2010, 312, 4.5 , 5   , 4   , 4.5 , 4.5],
             ['2015.03.13', 'Joseph Conrad'                              , 'POL', 'M', 'Mørkets hjerte'                     , 'Heart of Darkness'                                  , 1899, 128, 3   , 3   , 2   , 3.5 , 3  ],
             ['2015.01.30', 'Fjodor Dostojevskij'                        , 'RUS', 'M', 'Kældermennesket'                    , 'Notes from Underground'                             , 1864, 166, 4.5 , 4.5 , 3.5 , 4.5 , 4.5],
             ['2014.12.06', 'Charles Dickens'                            , 'ENG', 'M', 'En fortælling om to byer'           , 'A Tale of Two Cities'                               , 1859, 440, 3   , 3.5 , 2.5 , 3   , 2.5],
             ['2014.09.27', 'Gabriel García Marquéz'                     , 'COL', 'M', '100 års ensomhed'                   , 'One Hundred Years of Solitude'                      , 1967, 308, 1.5 , 3   , 2   , 3   , 3  ],
             ['2014.06.21', 'Knut Hamsun'                                , 'NOR', 'M', 'Sult'                               , 'Hunger'                                             , 1890, 108, 4.5 , 4.5 , 5   , 4   , 4.5],
             ['2014.06.21', 'Lewis Carroll'                              , 'ENG', 'M', 'Alice i Eventyrland'                , 'Alice In Wonderland'                                , 1865, 140, 3.5 , 4   , 2.5 , 3.5 , 3.5],
             ['2014.04.17', 'John Steinbeck'                             , 'USA', 'M', 'Øst for Paradis'                    , 'East Of Eden'                                       , 1952, 579, 4   , 4   , 4   , 4   , 4  ],
             ['2014.03.22', 'Ernest Hemingway'                           , 'USA', 'M', 'Den gamle mand og havet'            , 'The Old Man and the Sea'                            , 1952, 112, 3   , 3   , 3   , 3   , 3  ]]

    # Make arrays
    nbooks = len(books)

    date    = np.array([book[0] for book in books])
    author  = np.array([book[1] for book in books])
    country = np.array([book[2] for book in books])
    gender  = np.array([book[3] for book in books])
    titleDK = np.array([book[4] for book in books])
    titleEN = np.array([book[5] for book in books])
    year    = np.array([book[6] for book in books])
    pages   = np.array([book[7] for book in books])

    stars   = np.array([np.nanmean(book[8:13]) for book in books])
    spread  = np.array([np.nanstd (book[8:13]) for book in books])

    mikkel  = np.array([book[ 8] for book in books])
    morten  = np.array([book[ 9] for book in books])
    jeff    = np.array([book[10] for book in books])
    klaus   = np.array([book[11] for book in books])
    peter   = np.array([book[12] for book in books])

    if stats:
        print()
        print('Mikkel: {:.1f} ± {:.1f}'.format(np.nanmean(mikkel), np.nanstd(mikkel)))
        print('Morten: {:.1f} ± {:.1f}'.format(np.nanmean(morten), np.nanstd(morten)))
        print('Jeff:   {:.1f} ± {:.1f}'.format(np.nanmean(jeff  ), np.nanstd(jeff  )))
        print('Klaus:  {:.1f} ± {:.1f}'.format(np.nanmean(klaus ), np.nanstd(klaus )))
        print('Peter:  {:.1f} ± {:.1f}'.format(np.nanmean(peter ), np.nanstd(peter )))

    if language=='dk':
        title = titleDK
    else:
        title = titleEN
        author[np.where(author=='Os selv')] = 'Ourselves'

    if html:
        s0,s1      = '<strong>', '</strong>'
        len_author = max(len(a) for a in author)
        len_title  = max(len(t) for t in title) + len(s0+s1)

        curRead = '(læser i øjeblikket)' if language=='dk' else '(currently reading)'
        row0 = '<tr class="item">' \
             + '<td style="font-size:10px;">' + date[0]                           + '</td>' \
             + '<td>'                         + author[0].ljust(len_author)       + '</td>' \
             + '<td>'                         + country[0]                        + '</td>' \
             + '<td>'                         + (s0+title[0]+s1).ljust(len_title) + '</td>' \
             + '<td>'                         + str(year[0]).rjust(5)             + '</td>' \
             + '<td>'                         + str(pages[0]).zfill(3)            + '</td>' \
             + '<td colspan=2>'               + curRead                           + '</td>' \
             + '</tr>'
        print(row0)

        for i in range(1,nbooks):
            tit = title[i] if author[i]=='Os selv'   else s0+title[i]+s1
            tit = title[i] if author[i]=='Ourselves' else s0+title[i]+s1

            current_row = '<tr class="item">' \
                        + '<td style="font-size:10px;">' + date[i]                          + '</td>' \
                        + '<td>'                         + author[i].ljust(len_author)      + '</td>' \
                        + '<td>'                         + country[i]                       + '</td>' \
                        + '<td>'                         + tit.ljust(len_title)             + '</td>' \
                        + '<td>'                         + str(year[i]).rjust(5)            + '</td>' \
                        + '<td>'                         + str(pages[i]).zfill(3)           + '</td>' \
                        + '<td>'                         + '{:.1f}'.format(stars[i])        + '</td>' \
                        + '<td>'                         + '±' + '{:.1f}'.format(spread[i]) + '</td>' \
                        + '</tr>'
            print(current_row)

    if year_hist:
        fig = plt.figure(figsize=(6,4))
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('+590+480')
        bax = brokenaxes(xlims=((-2120,-2085),(-460,-435),(1740,1765),(1840,2030)),
                         ylims=None,
                         wspace=.05)
        bax.set_ylim([0,10])
        decades = np.arange(-2200,2040,10)
        bax.hist(year,bins=decades)
        if language=='dk':
            plt.xlabel('\nÅrstal',size=12)
            plt.ylabel('Antal bøger\n\n',size=12)
        else:
            plt.xlabel('\nYear',size=12)
            plt.ylabel('Number of books\n\n',size=12)
      # fig.tight_layout()
      # fig.subplots_adjust(bottom=0.15)
        xlim = bax.get_xlim()[0][0], bax.get_xlim()[-1][-1]
        ylim = bax.get_ylim()[0][0], bax.get_ylim()[-1][-1]
        bax.plot([xlim[1],xlim[1]], [ylim[0],ylim[1]],'k')
        bax.plot([xlim[0],xlim[1]], [ylim[1],ylim[1]],'k')

    if country_pie:
        unique_countries = np.unique(country,return_counts=True)
        name = unique_countries[0]
        freq = unique_countries[1]
      # nc = len(name)
      # others = 0
      # for i in range(nc):
      #     if freq[i] == 1:
      #         others += 1

        fig = plt.figure(figsize=(4,4))
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('+590+40')

        plt.pie(freq, labels=name,autopct='%1.1i%%')

    if page_hist:
        pass
      # plt.close('all')
      # fig,ax = plt.subplots()
      # dec30 = np.arange(1850,2040,10) # 1850, 1860, ..., 2030
      # ax.hist(published,bins=dec30)
      # dec20 = dec30[:-1]
      # dectix = [str(dec)+"'erne" for dec in dec20]
      # ax.set_xticks(dec20+5)
      # ax.set_xticklabels(dectix,size=8)
      # plt.xticks(rotation=45, ha='right')

      # plt.clf()
      # dec30 = np.arange(1850,2040,10) # 1850, 1860, ..., 2030
      # plt.hist(published,bins=dec30)
      # plt.xticks(np.arange(1850,2030,20))
      # plt.ylim([0,10])
      # if language=='dk':
      #     plt.xlabel('Årstal')
      #     plt.ylabel('Antal bøger')
      # else:
      #     plt.xlabel('Year')
      #     plt.ylabel('Number of books')
