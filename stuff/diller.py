import numpy as np

def dillit():
    
    grades = {  #                            Mi    Mo    Je    Kl    Pe
        'Vejene                             ': np.array([2   , 3.5 , 4.5 , 3   , 1.5]),
        'Leoparden                          ': np.array([2   , 3.5 , 1.5 , 3   , 3.5]),
      # 'Leoparden                          ': np.array([2,5 , 3   , 2   , 2.5 , 4  ]), # Kareten
        'Fluernes herre                     ': np.array([3   , 1.5 , 4   , 3.5 , 3.5]),
        'Krøniker fra Mars                  ': np.array([      4   , 2   , 3   , 4  ]),
        'Ørneborgen                         ': np.array([2.5 , 3.5 , 4   , 2   , 2.5]),
        'Lolita                             ': np.array([4.5 , 4   , 3.5 , 4   , 4.5]),
        'Salka Valka                        ': np.array([3   , 3   , 2   , 3   , 4  ]),
        'Tristram Shandys levned og meninger': np.array([2   , 3   , 3   , 3.5 , 2  ]),
        'En Fortælling om Blindhed          ': np.array([4   , 4.5 , 3.5 , 4   , 4.5]),
        'Hvepsefabrikken                    ': np.array([                        4  ]),
        'Harens år                          ': np.array([3.5 , 3   , 5   , 2.5 , 3.5]),
        'Den flammende verden               ': np.array([3.5 , 4.5 , 3   , 4   , 4  ]),
        'Stålhulerne                        ': np.array([1.5 , 1.5 , 2   , 1.5 , 2  ]),
        'Gilgamesh                          ': np.array([4   , 5   , 2.5 , 3.5 , 4  ]),
        'Under Nul                          ': np.array([2.5 , 3   , 4   , 2.5 , 2  ]),
        'Den store Gatsby                   ': np.array([2   , 1.5 , 4.5 , 2.5 , 2.5]),
        'Bliktrommen                        ': np.array([1   , 2   , 0   , 2   , 2.5]),
        'Rynkekneppesygen                   ': np.array([3.5 , 3.5 , 3.5 , 3.5 , 4  ]),
        'Mellem Himmel og Jord              ': np.array([4   , 4   , 4   , 4   , 4.5]),
        'Død på kredit                      ': np.array([5   , 5   , 5   , 5   , 4.5]),
        'Syv fantastiske fortællinger       ': np.array([2   , 2.5 , 1   , 2.5 , 3.5]),
        'Intet nyt fra Vestfronten          ': np.array([4   , 4.5 , 4.5 , 4.5 , 4  ]),
        'Slagterkoner og bagerenker         ': np.array([4.5 , 4   , 4.5 , 4   , 4  ]),
        'Radiator                           ': np.array([3.5 , 3   , 5   , 3.5 , 4  ]),
        'The Call of Cthulhu                ': np.array([4.5 , 4.5 , 2   , 4.5 , 4.5]),
        'Spionen der kom ind fra kulden     ': np.array([2   , 2   , 2.5 , 2   , 2.5]),
        'Historien om Job                   ': np.array([1   , 1.5 ,             0.5]),
        'Til Fyret                          ': np.array([2   , 2.5 , 2   , 3   , 3  ]),
        'En flygtning krydser sit spor      ': np.array([4.5 , 4.5 , 2   , 4.5 , 4.5]),
        'Planen                             ': np.array([4.5 , 4.5 , 4.5 , 3.5 , 4.5]),
        'Det Hvide Slot                     ': np.array([3.5 , 3.5       , 3.5 , 4  ]),
        'Det Dybe Net                       ': np.array([0.5 , 0.5 , 0   , 0.5 , 0.5]),
        'Vangede billeder                   ': np.array([4   , 3.5 , 4   , 3   , 3.5]),
        'Dræb ikke en sangfugl              ': np.array([3   , 3   , 3.5 , 3   , 3.5]),
        'Kortet og landskabet               ': np.array([4.5 , 5   , 4   , 4.5 , 4.5]),
        'Mørkets hjerte                     ': np.array([3   , 3   , 2   , 3.5 , 3  ]),
        'Kældermennesket                    ': np.array([4.5 , 4.5 , 3.5 , 4.5 , 4.5]),
        'En fortælling om to byer           ': np.array([3   , 3.5 , 2.5 , 3   , 2.5]),
        '100 års ensomhed                   ': np.array([1.5 , 3   , 2   , 3   , 3  ]),
        'Sult                               ': np.array([4.5 , 4.5 , 5   , 4   , 4.5]),
        'Alice i Eventyrland                ': np.array([3.5 , 4   , 2.5 , 3.5 , 3.5]),
        'Øst for Paradis                    ': np.array([4   , 4   , 4   , 4   , 4  ]),
        'Den gamle mand og havet            ': np.array([3   , 3   , 3   , 3   , 3  ])}

    Mikkel = []
    Morten = []
    Jeff   = []
    Klaus  = []
    Peter  = []

    for key, value in grades.items():
        print(key,'{:.1f} ± {:.1f}'.format(np.mean(value), np.std(value)))
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

    print()
    print('Mikkel: {:.1f} ± {:.1f}'.format(np.mean(Mikkel), np.std(Mikkel)))
    print('Morten: {:.1f} ± {:.1f}'.format(np.mean(Morten), np.std(Morten)))
    print('Jeff:   {:.1f} ± {:.1f}'.format(np.mean(Jeff  ), np.std(Jeff  )))
    print('Klaus:  {:.1f} ± {:.1f}'.format(np.mean(Klaus ), np.std(Klaus )))
    print('Peter:  {:.1f} ± {:.1f}'.format(np.mean(Peter ), np.std(Peter )))
