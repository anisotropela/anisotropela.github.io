import numpy as np

def dillit():
    #                       Mi  Mo  Je  Kl  Pe
    grades = {
        'Flammende      ': np.array([3.5 , 4.5 , 3   , 4   , 4  ]),
        'Staalhulerne   ': np.array([1.5 , 1.5 , 2   , 1.5 , 2  ]),
        'Gilgamesh      ': np.array([4   , 5   , 2.5 , 3.5 , 4  ]),
        'Under Nul      ': np.array([2.5 , 3   , 4   , 2.5 , 2  ]),
        'Gatsby         ': np.array([2   , 1.5 , 4.5 , 2.5 , 2.5]),
        'Bliktrommen    ': np.array([1   , 2   , 0   , 2   , 2.5]),
        'Rynkekneppe    ': np.array([3.5 , 3.5 , 3.5 , 3.5 , 4  ]),
        'Himmel og Jord ': np.array([4   , 4   , 4   , 4   , 4.5]),
        'Kredit         ': np.array([5   , 5   , 5   , 5   , 4.5]),
        'Syv fantastiske': np.array([2   , 2.5 , 1   , 2.5 , 3.5]),
        'Vestfronten    ': np.array([4   , 4.5 , 4.5 , 4.5 , 4  ]),
        'Slagterkoner   ': np.array([4.5 , 4   , 4.5 , 4   , 4  ]),
        'Radiator       ': np.array([3.5 , 3   , 5   , 3.5 , 4  ]),
        'Cthulhu        ': np.array([4.5 , 4.5 , 2   , 4.5 , 4.5]),
        'Spionen        ': np.array([2   , 2   , 2.5 , 2   , 2.5]),
        'Job            ': np.array([1   , 1.5 ,             0.5]),
        'Til Fyret      ': np.array([2   , 2.5 , 2   , 3   , 3  ]),
        'Flygtning      ': np.array([4.5 , 4.5 , 2   , 4.5 , 4.5]),
        'Planen         ': np.array([4.5 , 4.5 , 4.5 , 3.5 , 4.5]),
        'Det Hvide Slot ': np.array([3.5 , 3.5 , 0   , 3.5 , 4  ]),
        'Det Dybe Net   ': np.array([0.5 , 0.5 , 0   , 0.5 , 0.5]),
        'Vangede        ': np.array([4   , 3.5 , 4   , 3   , 3.5]),
        'Sangfugl       ': np.array([3   , 3   , 3.5 , 3   , 3.5]),
        'Kortet         ': np.array([4.5 , 5   , 4   , 4.5 , 4.5]),
        'Hjerte         ': np.array([3   , 3   , 2   , 3.5 , 3  ]),
        'Kaelder        ': np.array([4.5 , 4.5 , 3.5 , 4.5 , 4.5]),
        'To byer        ': np.array([3   , 3.5 , 2.5 , 3   , 2.5]),
        '100 aar        ': np.array([1.5 , 3   , 2   , 3   , 3  ]),
        'Sult           ': np.array([4.5 , 4.5 , 5   , 4   , 4.5]),
        'Alice          ': np.array([3.5 , 4   , 2.5 , 3.5 , 3.5]),
        'Paradis        ': np.array([4   , 4   , 4   , 4   , 4  ]),
        'Den Gamle Mand ': np.array([3   , 3   , 3   , 3   , 3  ])}

    Mikkel = []
    Morten = []
    Jeff   = []
    Klaus  = []
    Peter  = []

    for key, value in grades.items():
        print(key,'{:.1f} +\- {:.1f}'.format(np.mean(value), np.std(value)))
        try:
            Mikkel.append(value[0])
        except:
            pass
        try:
            Morten.append(value[1])
        except:
            pass
        try:
            Jeff.append(value[2])
        except:
            pass
        try:
            Klaus.append(value[3])
        except:
            pass
        try:
            Peter.append(value[4])
        except:
            pass

    print('Mikkel: {:.1f} +/- {:.1f}'.format(np.mean(Mikkel), np.std(Mikkel)))
    print('Morten: {:.1f} +/- {:.1f}'.format(np.mean(Morten), np.std(Morten)))
    print('Jeff:   {:.1f} +/- {:.1f}'.format(np.mean(Jeff  ), np.std(Jeff  )))
    print('Klaus:  {:.1f} +/- {:.1f}'.format(np.mean(Klaus ), np.std(Klaus )))
    print('Peter:  {:.1f} +/- {:.1f}'.format(np.mean(Peter ), np.std(Peter )))
