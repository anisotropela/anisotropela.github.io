import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes

def dillit(language      = 'dk',
           html          = False,
           year_hist     = True,
           page_hist     = True,
           star_hist     = True,
           country_pie   = True,
           all_countries = False,
           gender_pie    = True,
           title_en_vs_dk= True,
           agree_vs_time = True,
           correlate     = None,
           cxlim         = None,
           cylim         = None,
           corr_plot     = True,
           stats         = True,
           savefig       = False,
           ext           = '.png'
           ):
    """
    Landekoder følger FIFA: https://en.wikipedia.org/wiki/List_of_FIFA_country_codes
    >>> diller.dillit(language='dk',html=True,savefig=True)
    """
    assert language != 'da', "Brug language='dk' for dansk."
    plt.close('all')
    xyG = '?' # ' (Gilgamesh)' <- hvis strengen bliver længere, ændres figurens aspect ratio
    xyJ = '?'
    #                0          1                                            2     3       4                                       5                                                     6     7    8     9    10    11    12
    #                                                                                                                                                                                             Mi    Mo    Je    Kl    Pe
    books = [['2022.10.08', 'Luke Rhinehart'                             , 'USA', 'M', 'Terningenmanden'                      , 'The Dice Man'                                       , 1971, 477, nan , nan , nan , nan , nan],
             ['2022.08.26', 'Margaret Atwood'                            , 'CAN', 'F', 'Tjenerindens fortælling'              , 'The Handmaid\'s Tale'                               , 1985, 311, 2.5 , 3   , 3.5 , 3   , 3.5],
             ['2022.06.02', 'Jennifer Egan'                              , 'USA', 'F', 'Tæskeholdet banker på'                , 'A Visit from the Goon Squad'                        , 2010, 293, 4.0 , 4.0 , 4.0 , 4.0 , 4.0],
             ['2022.03.09', 'Hans Kirk'                                  , 'DEN', 'M', 'De ny tider'                          , 'De ny tider'                                        , 1939, 211, 3.0 , 3.5 , 2.5 , 3.0 , 4.0],
             ['2022.01.08', 'Lone Frank'                                 , 'DEN', 'F', 'Størst af alt'                        , 'Størst af alt'                                      , 2020, 292, 3.5 , 4   , 2   , 3   , 4  ],
             ['2021.10.29', 'Jack Kerouac'                               , 'USA', 'M', 'Vejene'                               , 'On the Road'                                        , 1957, 285, 2   , 3.5 , 4.5 , 3   , 1.5],
             ['2021.08.14', 'Giuseppe Tomasi di Lampedusa'               , 'ITA', 'M', 'Leoparden'                            , 'The Leopard'                                        , 1958, 247, 2   , 3.5 , 1.5 , 3   , 3.5],
             ['2021.06.12', 'William Golding'                            , 'ENG', 'M', 'Fluernes herre'                       , 'Lord of the Flies'                                  , 1954, 196, 3   , 1.5 , 4   , 3.5 , 3.5],
             ['2021.04.03', 'Ray Bradbury'                               , 'USA', 'M', 'Krøniker fra Mars'                    , 'The Martian Chronicles'                             , 1950, 192, nan , 4   , 2   , 3   , 4  ],
             ['2021.04.03', 'Alistair MacLean'                           , 'SCO', 'M', 'Ørneborgen'                           , 'Where Eagles Dare'                                  , 1967, 166, 2.5 , 3.5 , 4   , 2   , 2.5],
             ['2021.01.30', 'Vladimir Nabokov'                           , 'USA', 'M', 'Lolita'                               , 'Lolita'                                             , 1955, 307, 4.5 , 4   , 3.5 , 4   , 4.5],
             ['2020.11.21', 'Halldór Laxness'                            , 'ISL', 'M', 'Salka Valka'                          , 'Salka Valka'                                        , 1931, 373, 3   , 3   , 2   , 3   , 4  ],
             ['2020.09.18', 'Laurence Sterne'                            , 'ENG', 'M', 'Tristram Shandys levned og meninger'  , 'The Life and Opinions of Tristram Shandy, Gentleman', 1759, 588, 2   , 3   , 3   , 3.5 , 2  ],
             ['2020.05.30', 'José Saramago'                              , 'POR', 'M', 'En fortælling om blindhed'            , 'Blindness'                                          , 1995, 284, 4   , 4.5 , 3.5 , 4   , 4.5],
             ['2020.04.04', 'Iain M. Banks'                              , 'SCO', 'M', 'Hvepsefabrikken'                      , 'The Wasp Factory'                                   , 1984, 232, nan , nan , nan , nan , 4  ],
             ['2020.02.11', 'Arto Paasilinna'                            , 'FIN', 'M', 'Harens år'                            , 'The Year of the Hare'                               , 1975, 183, 3.5 , 3   , 5   , 2.5 , 3.5],
             ['2019.12.27', 'Siri Hustvedt'                              , 'USA', 'F', 'Den flammende verden'                 , 'The Blazing World'                                  , 2014, 434, 3.5 , 4.5 , 3   , 4   , 4  ],
             ['2019.10.26', 'Isaac Asimov'                               , 'USA', 'M', 'Stålhulerne'                          , 'Caves of Steel'                                     , 1953, 214, 1.5 , 1.5 , 2   , 1.5 , 2  ],
             ['2019.08.09', 'Sophus Helle og Morten Søndergaard (overs.)', 'SUM', xyG, 'Gilgamesh'                            , 'Gilgamesh'                                          ,-2100, 140, 4   , 5   , 2.5 , 3.5 , 4  ],
             ['2019.05.11', 'Brett Easton Ellis'                         , 'USA', 'M', 'Under nul'                            , 'Less than zero'                                     , 1985, 163, 2.5 , 3   , 4   , 2.5 , 2  ],
             ['2019.02.08', 'F. Scott Fitzgerald'                        , 'USA', 'M', 'Den store Gatsby'                     , 'The Great Gatsby'                                   , 1925, 171, 2   , 1.5 , 4.5 , 2.5 , 2.5],
             ['2018.11.24', 'Günther Grass'                              , 'GER', 'M', 'Bliktrommen'                          , 'The Tin Drum'                                       , 1959, 555, 1   , 2   , 0   , 2   , 2.5],
             ['2018.08.24', 'Peter Adolphsen'                            , 'DEN', 'M', 'Rynkekneppesygen'                     , 'Rynkekneppesygen'                                   , 2017, 245, 3.5 , 3.5 , 3.5 , 3.5 , 4  ],
             ['2018.06.02', 'Os selv'                                    , 'DEN', 'M', 'Vi skrev vores egne noveller'         , 'We wrote our own short stories'                     , 2018,  18, 5   , 5   , nan , nan , 5  ],
             ['2018.04.07', 'Svend Aage Madsen'                          , 'DEN', 'M', 'Mellem Himmel og Jord'                , 'Between Heaven and Earth'                           , 1990, 208, 4   , 4   , 4   , 4   , 4.5],
             ['2018.02.17', 'Louis-Ferdinand Céline'                     , 'FRA', 'M', 'Død på kredit'                        , 'Death on Credit'                                    , 1936, 508, 5   , 5   , 5   , 5   , 4.5],
             ['2017.12.15', 'Karen Blixen'                               , 'DEN', 'F', 'Syv fantastiske fortællinger'         , 'Seven Gothic Tales'                                 , 1934, 500, 2   , 2.5 , 1   , 2.5 , 3.5],
             ['2017.10.06', 'Erich Maria Remarque'                       , 'GER', 'M', 'Intet nyt fra Vestfronten'            , 'All Quiet on the Western Front'                     , 1929, 202, 4   , 4.5 , 4.5 , 4.5 , 4  ],
             ['2017.07.18', 'Jens Blendstrup'                            , 'DEN', 'M', 'Slagterkoner og bagerenker'           , 'Slagterkoner og Bagerenker'                         , 2016, 418, 4.5 , 4   , 4.5 , 4   , 4  ],
             ['2017.04.08', 'Jan Sonnergaard'                            , 'DEN', 'M', 'Radiator og andre noveller'           , 'Radiator and other short stories'                   , 1997, 221, 3.5 , 3   , 5   , 3.5 , 4  ],
             ['2017.02.10', 'H. P. Lovecraft'                            , 'USA', 'M', 'The Call of Cthulhu og andre noveller', 'The Call of Cthulhu and other short stories'        , 1928, 117, 4.5 , 4.5 , 2   , 4.5 , 4.5],
             ['2016.11.19', 'John le Carré'                              , 'ENG', 'M', 'Spionen der kom ind fra kulden'       , 'The Spy Who Came in from the Cold'                  , 1963, 225, 2   , 2   , 2.5 , 2   , 2.5],
             ['2016.08.26', 'Peter Madsen'                               , 'DEN', xyJ, 'Historien om Job'                     , 'The Book of Job (comic book version)'               , -450, 104, 1   , 1.5 , nan , nan , 0.5],
             ['2016.08.26', 'Virginia Woolf'                             , 'ENG', 'F', 'Til Fyret'                            , 'To the Lighthouse'                                  , 1927, 210, 2   , 2.5 , 2   , 3   , 3  ],
             ['2016.07.10', 'Aksel Sandemose'                            , 'DEN', 'M', 'En flygtning krydser sit spor'        , 'A Fugitive Crosses his Tracks'                      , 1933, 425, 4.5 , 4.5 , 2   , 4.5 , 4.5],
             ['2016.05.14', 'Morten Pape'                                , 'DEN', 'M', 'Planen'                               , 'Planen'                                             , 2015, 557, 4.5 , 4.5 , 4.5 , 3.5 , 4.5],
             ['2016.02.19', 'Orhan Pamuk'                                , 'TUR', 'M', 'Det hvide slot'                       , 'The White Castle'                                   , 1985, 160, 3.5 , 3.5 , nan , 3.5 , 4  ],
             ['2015.12.05', 'Thomas Pynchon'                             , 'USA', 'M', 'Det dybe net'                         , 'Bleeding Edge'                                      , 2013, 519, 0.5 , 0.5 , 0   , 0.5 , 0.5],
             ['2015.10.10', 'Dan Turèll'                                 , 'DEN', 'M', 'Vangede billeder'                     , 'Vangede Billeder'                                   , 1975, 193, 4   , 3.5 , 4   , 3   , 3.5],
             ['2015.08.28', 'Harper Lee'                                 , 'USA', 'F', 'Dræb ikke en sangfugl'                , 'To Kill a Mocking Bird'                             , 1960, 307, 3   , 3   , 3.5 , 3   , 3.5],
             ['2015.05.14', 'Michel Houellebecq'                         , 'FRA', 'M', 'Kortet og landskabet'                 , 'The Map and the Territory'                          , 2010, 312, 4.5 , 5   , 4   , 4.5 , 4.5],
             ['2015.03.13', 'Joseph Conrad'                              , 'POL', 'M', 'Mørkets hjerte'                       , 'Heart of Darkness'                                  , 1899, 128, 3   , 3   , 2   , 3.5 , 3  ],
             ['2015.01.30', 'Fjodor Dostojevskij'                        , 'RUS', 'M', 'Kældermennesket'                      , 'Notes from Underground'                             , 1864, 166, 4.5 , 4.5 , 3.5 , 4.5 , 4.5],
             ['2014.12.06', 'Charles Dickens'                            , 'ENG', 'M', 'En fortælling om to byer'             , 'A Tale of Two Cities'                               , 1859, 440, 3   , 3.5 , 2.5 , 3   , 2.5],
             ['2014.09.27', 'Gabriel García Marquéz'                     , 'COL', 'M', '100 års ensomhed'                     , 'One Hundred Years of Solitude'                      , 1967, 308, 1.5 , 3   , 2   , 3   , 3  ],
             ['2014.06.21', 'Knut Hamsun'                                , 'NOR', 'M', 'Sult'                                 , 'Hunger'                                             , 1890, 108, 4.5 , 4.5 , 5   , 4   , 4.5],
             ['2014.06.21', 'Lewis Carroll'                              , 'ENG', 'M', 'Alice i Eventyrland'                  , 'Alice In Wonderland'                                , 1865, 140, 3.5 , 4   , 2.5 , 3.5 , 3.5],
             ['2014.04.17', 'John Steinbeck'                             , 'USA', 'M', 'Øst for Paradis'                      , 'East Of Eden'                                       , 1952, 579, 4   , 4   , 4   , 4   , 4  ],
             ['2014.03.22', 'Ernest Hemingway'                           , 'USA', 'M', 'Den gamle mand og havet'              , 'The Old Man and the Sea'                            , 1952, 112, 3   , 3   , 3   , 3   , 3  ]]

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
  # print(np.nanmean(pages),'±',np.nanstd(pages))

    stars     = np.array([np.nanmean(book[8:13]) for book in books])
    spread    = np.array([np.nanstd (book[8:13]) for book in books])
    med = np.array([np.nanpercentile(book[8:13],50) for book in books])
    lo = np.array([np.nanpercentile(book[8:13],15.9) for book in books])
    hi = np.array([np.nanpercentile(book[8:13],84.1) for book in books])

    if language=='dk':
        title = titleDK
        dillertable = 'dillertableDK.html'
    else:
        title = titleEN
        dillertable = 'dillertableEN.html'
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
             + '</tr>\n'
        with open(dillertable, 'w') as myfile: myfile.write(row0)

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
                        + '</tr>\n'
            with open(dillertable, 'a') as myfile: myfile.write(current_row)

    if year_hist:
        fig = plt.figure()
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('600x475+570+500')
        bax = brokenaxes(xlims=((-2120,-2085),(-460,-435),(1740,1765),(1840,2030)),
                         ylims=None,
                         wspace=.05)
        bax.set_ylim([0,10])
        decades = np.arange(-2200,2050,10)
        bax.hist(year,bins=decades,color='g',alpha=.25,histtype='stepfilled')
        bax.hist(year,bins=decades,   ec='g',          histtype='step')
        if language=='dk':
            plt.xlabel('\nÅrstal',size=14)
            plt.ylabel('Antal bøger\n\n',size=14)
        else:
            plt.xlabel('\nYear',size=14)
            plt.ylabel('Number of books\n\n',size=14)
      # fig.tight_layout()
      # fig.subplots_adjust(bottom=0.15)
        xlim = bax.get_xlim()[0][0], bax.get_xlim()[-1][-1]
        ylim = bax.get_ylim()[0][0], bax.get_ylim()[-1][-1]
        bax.plot([xlim[1],xlim[1]], [ylim[0],ylim[1]],'k')
        bax.plot([xlim[0],xlim[1]], [ylim[1],ylim[1]],'k')
        if savefig: plt.savefig('year_hist_'+language+ext, dpi=300, bbox_inches='tight')

    if country_pie:
        unique_countries = np.unique(country,return_counts=True)
        name = unique_countries[0]
        freq = unique_countries[1]

        ionce = np.where(freq==1)
        name_once = name[ionce]
        freq_once = len(ionce[0])
        label_once = 'Other\ncountries' # '+'.join(name_once)
        name_oncesumd = np.append(np.delete(name,ionce), label_once)
        freq_oncesumd = np.append(np.delete(freq,ionce), freq_once)

        fig = plt.figure()
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('400x450+570+25')

        if all_countries:
            plt.pie(freq, labels=name,autopct='%1.1i%%')
        else:
            plt.pie(freq_oncesumd, labels=name_oncesumd,autopct='%1.1i%%')
        if savefig: plt.savefig('country_pie'+'_'+language+ext, dpi=300, bbox_inches='tight')

    if page_hist:
        fig,ax = plt.subplots()
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('600x480+975+25')
        ax.hist(pages,color='orange',alpha=.25,bins=range(0,651,50),histtype='stepfilled')
        ax.hist(pages,   ec='orange',          bins=range(0,651,50),histtype='step')
        if language=='dk':
            ax.set_xlabel('Antal sider',fontsize=14)
            ax.set_ylabel('Antal bøger',fontsize=14)
        else:
            ax.set_xlabel('Number of pages',fontsize=14)
            ax.set_ylabel('Number of books',fontsize=14)
        if savefig: plt.savefig('page_hist_'+language+ext, dpi=300, bbox_inches='tight')

    if gender_pie:
        fig = plt.figure(figsize=(4,4))
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('400x450+1175+500')

        unique_gender = np.unique(gender,return_counts=True)
        name = unique_gender[0]
        freq = unique_gender[1]
        plt.pie(freq, labels=name,autopct='%1.1i%%')
        if savefig: plt.savefig('gender_pie_'+language+ext, dpi=300, bbox_inches='tight')

    if star_hist:
        mikkel  = np.array([book[ 8] for book in books])
        morten  = np.array([book[ 9] for book in books])
        jeff    = np.array([book[10] for book in books])
        klaus   = np.array([book[11] for book in books])
        peter   = np.array([book[12] for book in books])
        diller  = np.concatenate((mikkel,morten,jeff,klaus,peter))

        mumi  = np.nanmean(mikkel); smumi  = '{:.1f}'.format(mumi )
        mumo  = np.nanmean(morten); smumo  = '{:.1f}'.format(mumo )
        muje  = np.nanmean(jeff  ); smuje  = '{:.1f}'.format(muje )
        mukl  = np.nanmean(klaus ); smukl  = '{:.1f}'.format(mukl )
        mupe  = np.nanmean(peter ); smupe  = '{:.1f}'.format(mupe )
        mudi  = np.nanmean(diller); smudi  = '{:.1f}'.format(mudi )
        sigmi = np.nanstd(mikkel) ; ssigmi = '{:.1f}'.format(sigmi)
        sigmo = np.nanstd(morten) ; ssigmo = '{:.1f}'.format(sigmo)
        sigje = np.nanstd(jeff  ) ; ssigje = '{:.1f}'.format(sigje)
        sigkl = np.nanstd(klaus ) ; ssigkl = '{:.1f}'.format(sigkl)
        sigpe = np.nanstd(peter ) ; ssigpe = '{:.1f}'.format(sigpe)
        sigdi = np.nanstd(diller) ; ssigdi = '{:.1f}'.format(sigdi)
        medmi,lomi,himi = np.nanpercentile(mikkel,[50,15.9,84.1]) ; smedmi   = '{:.1f}'.format(medmi  )
        medmo,lomo,himo = np.nanpercentile(morten,[50,15.9,84.1]) ; smedmo   = '{:.1f}'.format(medmo  )
        medje,loje,hije = np.nanpercentile(jeff  ,[50,15.9,84.1]) ; smedje   = '{:.1f}'.format(medje  )
        medkl,lokl,hikl = np.nanpercentile(klaus ,[50,15.9,84.1]) ; smedkl   = '{:.1f}'.format(medkl  )
        medpe,lope,hipe = np.nanpercentile(peter ,[50,15.9,84.1]) ; smedpe   = '{:.1f}'.format(medpe  )
        meddi,lodi,hidi = np.nanpercentile(diller,[50,15.9,84.1]) ; smeddi   = '{:.1f}'.format(meddi  )
        siglomi = medmi - lomi                                 ; ssiglomi = '{:.1f}'.format(siglomi)
        siglomo = medmo - lomo                                 ; ssiglomo = '{:.1f}'.format(siglomo)
        sigloje = medje - loje                                 ; ssigloje = '{:.1f}'.format(sigloje)
        siglokl = medkl - lokl                                 ; ssiglokl = '{:.1f}'.format(siglokl)
        siglope = medpe - lope                                 ; ssiglope = '{:.1f}'.format(siglope)
        siglodi = meddi - lodi                                 ; ssiglodi = '{:.1f}'.format(siglodi)
        sighimi = himi - medmi                                 ; ssighimi = '{:.1f}'.format(sighimi)
        sighimo = himo - medmo                                 ; ssighimo = '{:.1f}'.format(sighimo)
        sighije = hije - medje                                 ; ssighije = '{:.1f}'.format(sighije)
        sighikl = hikl - medkl                                 ; ssighikl = '{:.1f}'.format(sighikl)
        sighipe = hipe - medpe                                 ; ssighipe = '{:.1f}'.format(sighipe)
        sighidi = hidi - meddi                                 ; ssighidi = '{:.1f}'.format(sighidi)

      # print()
      # print('Mikkel: '+smumi+' ± '+ssigmi)
      # print('Morten: '+smumo+' ± '+ssigmo)
      # print('Jeff:   '+smuje+' ± '+ssigje)
      # print('Klaus:  '+smukl+' ± '+ssigkl)
      # print('Peter:  '+smupe+' ± '+ssigpe)
      # print('Diller: '+smudi+' ± '+ssigdi)

      # labmi  = 'Mikkel:  '    +r'$'+smumi+'\pm'+ssigmi+'$'
      # labmo  = 'Morten: '     +r'$'+smumo+'\pm'+ssigmo+'$'
      # labje  = 'Jeff:       ' +r'$'+smuje+'\pm'+ssigje+'$'
      # labkl  = 'Klaus:    '   +r'$'+smukl+'\pm'+ssigkl+'$'
      # labpe  = 'Peter:    '   +r'$'+smupe+'\pm'+ssigpe+'$'
      # labdi  = 'Diller:   '   +r'$'+smudi+'\pm'+ssigdi+'$'

        labmi  = 'Mikkel:  '    +r'$'+smumi+'_{-'+ssiglomi+'}^{+'+ssighimi+'}$'
        labmo  = 'Morten: '     +r'$'+smumo+'_{-'+ssiglomo+'}^{+'+ssighimo+'}$'
        labje  = 'Jeff:       ' +r'$'+smuje+'_{-'+ssigloje+'}^{+'+ssighije+'}$'
        labkl  = 'Klaus:    '   +r'$'+smukl+'_{-'+ssiglokl+'}^{+'+ssighikl+'}$'
        labpe  = 'Peter:    '   +r'$'+smupe+'_{-'+ssiglope+'}^{+'+ssighipe+'}$'
        labdi  = r'$\mathbf{Diller:\,'+smudi+'_{-'+ssiglodi+'}^{+'+ssighidi+'}}$'

      # print('labmi    =', labmi)
      # print('labmo    =', labmo)
      # print('labje    =', labje)
      # print('labkl    =', labkl)
      # print('labpe    =', labpe)
      # print('labdi    =', labdi)

        fig,ax = plt.subplots()
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('560x480+1+500')
        ax.hist(mikkel,  color='c',alpha=.05,label=labmi,bins=np.linspace(-.25,5.25,12),histtype='stepfilled')
        ax.hist(mikkel,     ec='c',                      bins=np.linspace(-.25,5.25,12),histtype='step')
        ax.hist(morten,  color='m',alpha=.05,label=labmo,bins=np.linspace(-.25,5.25,12),histtype='stepfilled')
        ax.hist(morten,     ec='m',                      bins=np.linspace(-.25,5.25,12),histtype='step')
        ax.hist(jeff  ,  color='y',alpha=.05,label=labje,bins=np.linspace(-.25,5.25,12),histtype='stepfilled')
        ax.hist(jeff  ,     ec='y',                      bins=np.linspace(-.25,5.25,12),histtype='step')
        ax.hist(klaus ,  color='r',alpha=.05,label=labkl,bins=np.linspace(-.25,5.25,12),histtype='stepfilled')
        ax.hist(klaus ,     ec='r',                      bins=np.linspace(-.25,5.25,12),histtype='step')
        ax.hist(peter ,  color='g',alpha=.05,label=labpe,bins=np.linspace(-.25,5.25,12),histtype='stepfilled')
        ax.hist(peter ,     ec='g',                      bins=np.linspace(-.25,5.25,12),histtype='step')

        (counts, bins) = np.histogram(diller, bins=np.linspace(-.25,5.25,12))
      # ax.hist(diller,color='k',alpha=.05,label=labdi,bins=np.linspace(-.25,5.25,12),histtype='stepfilled')
      # ax.hist(diller,   ec='k',          label=labdi,bins=np.linspace(-.25,5.25,12),histtype='step')
        ax.hist(bins[:-1],bins,ec='k',label=labdi,weights=counts/5, histtype='step',lw=2,ls=':')
        ax.hist(bins[:-1],bins,ec='k',            weights=counts/5, histtype='step',lw=.5,ls='-')

        leg = ax.legend(loc='upper left')
        for lh in leg.legendHandles:
            lh.set_alpha(.5)

        if language=='dk':
            ax.set_xlabel('Antal stjerner', fontsize=14)
            ax.set_ylabel('Hyppighed', fontsize=14)
        else:
            ax.set_xlabel('Rating', fontsize=14)
            ax.set_ylabel('Frequency', fontsize=14)
        if savefig: plt.savefig('star_hist_'+language+ext, dpi=300, bbox_inches='tight')

    if False:#correlate is not None:
        """
        https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib
        https://www.google.com/search?client=safari&rls=en&q=python+plot+date+on+x+axis&ie=UTF-8&oe=UTF-8
        https://stackoverflow.com/questions/43133605/convert-integer-yyyymmdd-to-date-format-mm-dd-yyyy-in-python
        https://stackoverflow.com/questions/29779155/converting-string-yyyy-mm-dd-into-datetime
        https://stackoverflow.com/questions/466345/converting-string-into-datetime
        """
        from datetime import datetime
        import matplotlib.dates as mdates
      # xx = globals()#[correlate]
      # x = locals()[correlate[0]]
      # y = locals()[correlate[1]]

        fig,ax = plt.subplots()
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('600x500+750+400')

      # ax.scatter(x,y)
      # ax.set_xlabel(correlate[0])
      # ax.set_ylabel(correlate[1])
      # if cxlim is not None: ax.set_xlim(cxlim)
      # if cylim is not None: ax.set_ylim(cylim)

      # x = np.array([len(t) for t in titleDK])
      # y = np.array([len(t) for t in titleEN])
      # ax.scatter(x,y)

      # x = np.array([len(a) for a in author])
      # y = np.array([len(t) for t in titleDK])
      # ax.scatter(x,y)

      # x = range(nbooks)
      # y = spread
      # ax.scatter(x,y)

        lentit = np.array([len(t) for t in titleDK])
        lenaut = np.array([len(a) for a in author])
      # x = lentit                                  # stig
      # x = lenaut                                  # ret (fald stig)
      # x = year ; ax.set_xlim([1750,2021])         # fald stig
      # x = range(nbooks)                           # spred
      # x = pages                                   # spred
      # x = abs(year-1957)
        x = [datetime.strptime(d,'%Y.%m.%d').date() for d in date]

        y = stars # med VEND DENNE AKSE LISSOM I AGREE_VS_TIME

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        ax.errorbar(x,y, yerr=[y-lo,hi-y], fmt='ro',mec='r',alpha=1,
                elinewidth=1,capthick=1,ecolor='r',capsize=3)
        ax.scatter(x,y,c='r')
        plt.gcf().autofmt_xdate()

    if title_en_vs_dk:
        """
        """
        fig,ax = plt.subplots()
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('500x546+750+400')

        x = [len(t) for t in titleDK]
        y = [len(t) for t in titleEN]

        ax.scatter(x,y,c='r')
        ax.plot([0,50],[0,50],'k--',alpha=.5)
        if language=='dk':
            ax.set_xlabel('Dansk titellængde', fontsize=14)
            ax.set_ylabel('Engelsk titellængde', fontsize=14)
        else:
            ax.set_xlabel('Length of Danish title', fontsize=14)
            ax.set_ylabel('Length of English title', fontsize=14)
        ax.set_xlim([0,50])
        ax.set_ylim([0,50])
        if savefig: plt.savefig('title_en_vs_dk_'+language+ext, dpi=300, bbox_inches='tight')

    if agree_vs_time:
        fig,ax = plt.subplots()
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('600x500+850+500')

        x = range(nbooks)
        y = stars[::-1] # med

        ax.errorbar(x,y, yerr=[y-lo[::-1],hi[::-1]-y], fmt='ro',mec='r',alpha=1,
                elinewidth=1,capthick=1,ecolor='r',capsize=3)
        ax.scatter(x,y,c='r')
        if language=='dk':
            ax.set_xlabel('Møde #', fontsize=14)
            ax.set_ylabel('Antal stjerner (error bars viser 1'+r'$\sigma$'+')', fontsize=14)
        else:
            ax.set_xlabel('Meeting #', fontsize=14)
            ax.set_ylabel('Rating (error bars denote 1'+r'$\sigma$'+')', fontsize=14)
        if savefig: plt.savefig('agree_vs_time_'+language+ext, dpi=300, bbox_inches='tight')

    if corr_plot:
        fig,ax = plt.subplots()
        wm = plt.get_current_fig_manager()
        wm.window.wm_geometry('600x500+950+600')

      # x = np.array([len(a) for a in author])
      # y = np.array([len(t) for t in titleDK])
      # ax.scatter(x,y)

      # x = range(nbooks)
      # y = spread
      # ax.scatter(x,y)

        lentit = np.array([len(t) for t in titleDK])
        lenaut = np.array([len(a) for a in author])
      # x = lenaut                                  # ret (fald stig)
      # y = lentit                                  # stig
      # x = year ; ax.set_xlim([1750,2021])         # fald stig
      # x = range(nbooks)                           # spred
      # x = pages                                   # spred
      # x = year / pages ; ax.set_xlim([0,20])      # 
      # x = year-1957 ; ax.set_xlim([-100,100])
        x = year / lenaut
        klaus   = np.array([book[11] for book in books])
        y = pages * klaus

      # y = stars # med

      # ax.errorbar(x,y, yerr=[y-lo,hi-y], fmt='ro',mec='r',alpha=1,
      #         elinewidth=1,capthick=1,ecolor='r',capsize=3)
        ax.scatter(x,y,c='r')
        ax.set_xlim([0,250])
        ax.set_ylim([0,3000])
        ax.set_xlabel('[Udgivelsesår]  /  [Længden af forfatterens navn]', fontsize=14)
        ax.set_ylabel('[Antal sider]  ' + r'$\times$' + '  [Klaus\' rating]', fontsize=14)
        if savefig: plt.savefig('corr_plot_'+language+ext, dpi=300, bbox_inches='tight')

        if stats:
            mu,std    = np.nanmean(pages), np.nanstd(pages)
            med,lo,hi = np.nanpercentile(pages,[50,15.9,84.1])
            print('Sider, ave+1sig: ', mu,std)
            print('Sider, med+perc: ', med,lo,hi)
            print('        =>       ', med,med-lo,hi-med)
