import numpy as np
from numpy import pi,exp,sqrt
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from astropy import units as u
from astropy.cosmology import Planck18
from astropy.cosmology import FlatLambdaCDM
from astropy.cosmology import z_at_value
import astropy.constants as cc
import sys
sys.path.append('/Users/pela/Projects/z8p8/MassFunction')
from MF_Odense import dNdlnM

#cosmo = FlatLambdaCDM(H0=70, Om0=.3)
cosmo = Planck18
mH = cc.m_p + cc.m_e
kB = cc.k_B
G  = cc.G

# def schechter(phistar,Lstar,alpha):
#     """few"""
#     L_Ls = (L / Lstar).decompose().value
#     phi = phistar * L_Ls**alpha * exp(-L_Ls) / 
# 

#------------------------------------------------------------------------------

def redshift_records(cosmo=Planck18):
    """
    From https://en.wikipedia.org/wiki/List_of_the_most_distant_astronomical_objects#Timeline_of_most_distant_astronomical_object_recordholders
    HD1 not included, because 4 sigma signal of a 4 sigma detection isn't good enough...
    """
    wikilist = [['GN-z11'         ,'Galaxy', 2016, 2022, 11.09  ,'r'],
                ['EGSY8p7'        ,'Galaxy', 2015, 2016,  8.68  ,'r'],
                ['GRB090423'      ,'GRB'   , 2009, 2015,  8.2   ,'c'],
                ['IOK-1'          ,'Galaxy', 2006, 2009,  6.96  ,'r'],
                ['SDFJ1325'       ,'Galaxy', 2005, 2006,  6.597 ,'r'],
                ['SDFJ1324'       ,'Galaxy', 2003, 2005,  6.578 ,'r'],
                ['HCM-6A'         ,'Galaxy', 2002, 2003,  6.56  ,'r'],
                ['J1030'          ,'Quasar', 2001, 2002,  6.28  ,'b'],
                ['SDSS1044'       ,'Quasar', 2000, 2001,  5.82  ,'b'],
                ['SSA22-HCM1'     ,'Galaxy', 1999, 2000,  5.74  ,'r'],
                ['HDF4-473.0'     ,'Galaxy', 1998, 1999,  5.60  ,'r'],
                ['RD1'            ,'Galaxy', 1998, 1998,  5.34  ,'r'],
                ['CL1358+62 G1/2' ,'Galaxy', 1997, 1998,  4.92  ,'r'],
                ['PC1247'         ,'Quasar', 1991, 1997,  4.897 ,'b'],
                ['PC1158'         ,'Quasar', 1989, 1991,  4.73  ,'b'],
                ['Q0051'          ,'Quasar', 1987, 1989,  4.43  ,'b'],
                ['Q0000'          ,'Quasar', 1987, 1987,  4.11  ,'b'],
                ['PC0910'         ,'Quasar', 1987, 1987,  4.04  ,'b'],
                ['Q0046'          ,'Quasar', 1987, 1987,  4.01  ,'b'],
                ['Q1208'          ,'Quasar', 1986, 1987,  3.80  ,'b'],
                ['PKS2000'        ,'Quasar', 1982, 1986,  3.78  ,'b'],
                ['OQ172'          ,'Quasar', 1974, 1982,  3.53  ,'b'],
                ['OH471'          ,'Quasar', 1973, 1974,  3.408 ,'b'],
                ['4C05.34'        ,'Quasar', 1970, 1973,  2.877 ,'b'],
                ['5C02.56'        ,'Quasar', 1968, 1970,  2.399 ,'b'],
                ['4C25.05'        ,'Quasar', 1968, 1968,  2.358 ,'b'],
                ['PKS0237'        ,'Quasar', 1967, 1968,  2.225 ,'b'],
                ['4C12.39'        ,'Quasar', 1966, 1967,  2.1291,'b'],
                ['4C01.02'        ,'Quasar', 1965, 1966,  2.0990,'b'],
                ['3C9'            ,'Quasar', 1965, 1965,  2.018 ,'b'],
                ['3C147'          ,'Quasar', 1964, 1965,  0.545 ,'b'],
                ['3C295'          ,'Galaxy', 1960, 1964,  0.461 ,'r'],
                ['LEDA25177'      ,'Galaxy', 1951, 1960,  0.2   ,'r'],
                ['LEDA51975'      ,'Galaxy', 1936, 1936,  0.13  ,'r'],
                ['LEDA20221'      ,'Galaxy', 1932, 1932,  0.075 ,'r'],
                ['BCG/Leo'        ,'Galaxy', 1931, 1932,  0.066 ,'r'],
                ['BCG/Ursa Major' ,'Galaxy', 1930, 1931,  0.039 ,'r'],
                ['NGC4860'        ,'Galaxy', 1929, 1930,  0.026 ,'r'],
                ['NGC7619'        ,'Galaxy', 1929, 1929,  0.012 ,'r'],
                ['NGC584'         ,'Galaxy', 1921, 1929,  0.006 ,'r'],
                ['M104'           ,'Galaxy', 1913, 1921,  0.004 ,'r']]

    name = [obj[0] for obj in wikilist][::-1]
    what = [obj[1] for obj in wikilist][::-1]
    yr0  = [obj[2] for obj in wikilist][::-1]
    yr1  = [obj[3] for obj in wikilist][::-1]
    z    = [obj[4] for obj in wikilist][::-1]
    col  = [obj[5] for obj in wikilist][::-1]

    d    = cosmo.comoving_distance(z)
    t    = cosmo.age(z)
    d11  = cosmo.comoving_distance(11.09)
    z17  = 16.
    d17  = cosmo.comoving_distance(z17)
    t11  = cosmo.age(11.09)
    t17  = cosmo.age(z17)

    nobj = len(wikilist)
    yax  = np.arange(yr0[0],yr1[-1])

    plt.clf()
    plt.plot(yr0,t,'k-',lw=1)
    plt.scatter(yr0,t,s=50,color=col,zorder=10)
    plt.plot([2016,2022],[t11.value,t17.value],ls='--',c='lightgray',lw=1)
    plt.scatter([2022],[t17.value],s=50,color='lightgray')
    plt.scatter([2022],[1.1*t17.value],s=50,color='lightgray',alpha=.5)
    plt.scatter([2022],[t17.value/1.1],s=50,color='lightgray',alpha=.5)
    plt.scatter([2022],[1.2*t17.value],s=50,color='lightgray',alpha=.25)
    plt.scatter([2022],[t17.value/1.2],s=50,color='lightgray',alpha=.25)
    plt.scatter([2022],[1.3*t17.value],s=50,color='lightgray',alpha=.1)
    plt.scatter([2022],[t17.value/1.3],s=50,color='lightgray',alpha=.1)
    if True:
        plt.scatter(0,1,s=50,color='r',label='Galaxy')
        plt.scatter(0,1,s=50,color='b',label='Quasar')
        plt.scatter(0,1,s=50,color='c',label='GRB')

    plt.annotate('?', color='gray', xy=[2018,.22],fontsize=12)

  # plt.xscale('log')
    plt.yscale('log')
    plt.xlim([1910,2023])
    ylim = [.08,20]
    plt.ylim(ylim)
    ax = plt.gca()
    ax.set_yticks([.1,.2,.4,1,3,10,13.8])
    ax.set_yticklabels(['100 Myr','200 Myr','400 Myr','1 Gyr','3 Gyr','10 Gyr','13.8 Gyr'])
    plt.xlabel('Year of discovery',fontsize=16)
    plt.ylabel('Age of the Universe',fontsize=16)
    plt.legend()

    ax2   = plt.twinx()
    ylim2 = ylim
    ax2.set_ylim(ylim2)
    ax2.set_yscale('log')
    zmarks = [0,.5,1,2,5,10,13,20,30]
    tmarks = cosmo.age(zmarks)
    ax2.set_yticks(tmarks.value)
    ax2.set_yticklabels(zmarks)
    ax2.set_ylabel('Redshift',fontsize=16)

  # plt.fill_between([0,3e3],[.1,.1],[.20,.20],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.19,.19],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.18,.18],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.17,.17],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.16,.16],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.15,.15],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.14,.14],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.13,.13],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.12,.12],color='yellow',alpha=.1)
  # plt.fill_between([0,3e3],[.1,.1],[.11,.11],color='yellow',alpha=.1)
    plt.fill_between([0,3e3],[.0,.0],[.200,.200],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.199,.199],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.198,.198],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.197,.197],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.196,.196],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.195,.195],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.194,.194],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.193,.193],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.192,.192],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.191,.191],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.190,.190],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.189,.189],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.188,.188],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.187,.187],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.186,.186],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.185,.185],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.184,.184],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.183,.183],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.182,.182],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.181,.181],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.180,.180],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.179,.179],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.178,.178],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.177,.177],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.176,.176],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.175,.175],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.174,.174],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.173,.173],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.172,.172],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.171,.171],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.170,.170],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.169,.169],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.168,.168],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.167,.167],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.166,.166],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.165,.165],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.164,.164],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.163,.163],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.162,.162],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.161,.161],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.160,.160],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.159,.159],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.158,.158],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.157,.157],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.156,.156],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.155,.155],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.154,.154],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.153,.153],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.152,.152],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.151,.151],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.150,.150],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.149,.149],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.148,.148],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.147,.147],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.146,.146],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.145,.145],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.144,.144],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.143,.143],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.142,.142],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.141,.141],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.140,.140],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.139,.139],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.138,.138],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.137,.137],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.136,.136],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.135,.135],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.134,.134],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.133,.133],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.132,.132],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.131,.131],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.130,.130],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.129,.129],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.128,.128],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.127,.127],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.126,.126],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.125,.125],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.124,.124],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.123,.123],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.122,.122],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.121,.121],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.120,.120],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.119,.119],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.118,.118],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.117,.117],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.116,.116],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.115,.115],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.114,.114],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.113,.113],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.112,.112],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.111,.111],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.110,.110],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.109,.109],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.108,.108],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.107,.107],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.106,.106],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.105,.105],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.104,.104],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.103,.103],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.102,.102],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.101,.101],color='k',alpha=.0095)
    plt.fill_between([0,3e3],[.0,.0],[.100,.100],color='k',alpha=1)

    plt.annotate('', xy=(2010,.1),  # arrowhead coords
            xytext=(2010,.2),                 # text coords
            arrowprops=dict(
                color='k',
                lw=6,
                capstyle='butt',
                joinstyle='miter',
                arrowstyle='<->'
                ))

    plt.annotate('', xy=(2010,.103),  # arrowhead coords
            xytext=(2010,.195),                 # text coords
            arrowprops=dict(
                color='yellow',
                lw=4,
                capstyle='butt',
                joinstyle='miter',
                arrowstyle='<->'
                ))

    plt.annotate('We think the first stars\nand galaxies appeared\nsometime around here',
            fontsize=8,
            color='yellow',
            xy=(1975,.11))
#------------------------------------------------------------------------------

def nH(z,cosmo=Planck18):
    """
    Number density of hydrogen atoms as a function of redshift.
    """
    return (cosmo.critical_density(z) * cosmo.Ob(z) / mH).to(u.m**-3)
#------------------------------------------------------------------------------

def redshift_lookback(cosmo=Planck18):
    z  = np.logspace(4,-4,801)
    t  = Planck18.age(z)
    d  = Planck18.comoving_distance(z).to(u.Mlyr).value
    tL = Planck18.lookback_time(z)

    plt.clf()
    xlim = [0,13] # z
    ylim = [0,14] # lookback
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('Redshift '+r'$(z)$',fontsize=16)
    plt.ylabel('Billion years ago',fontsize=16)
    plt.plot(z,tL,'-r',lw=2)
  # plt.xscale('log')

    zGNz11  = 11.09
    dGNz11  = cosmo.comoving_distance(zGNz11)
    tLGNz11 = cosmo.lookback_time(zGNz11)
    plt.scatter(zGNz11,tLGNz11,color='r',s=50)

    ax2   = plt.twinx()
    ylim2 = ylim
    ax2.set_ylim(ylim2)
  # dmarks = [5,10,20,30,round(dGNz11.to(u.Glyr).value,1),35]
    dmarks = [1,5,10,20,30]
    zmarks = [z_at_value(cosmo.comoving_distance,dd*u.Glyr) for dd in dmarks]
    tLmarks = [cosmo.lookback_time(zz).value for zz in zmarks]
    ax2.set_yticks(tLmarks)
    ax2.set_yticklabels(dmarks)
    ax2.set_ylabel('Current distance / Glyr',fontsize=16)

    ax3   = plt.twiny()
    xlim2 = xlim
    ax3.set_xlim(xlim2)
  # dmarks = [5,10,20,30,round(dGNz11.to(u.Glyr).value,1),35]
    rhomarks = [1,3,10,30,100,300]
    zmarks = [z_at_value(nH,rr*u.m**-3) for rr in rhomarks]
    ax3.set_xticks(zmarks)
    ax3.set_xticklabels(rhomarks)
    ax3.set_xlabel('Average number density of atoms / m'+r'$^{-3}$',fontsize=16)

    plt.savefig('redshift.pdf',dpi=300, box_inches='tight')
#------------------------------------------------------------------------------

def cooling_function_from_file(file='cooling_function_Z0.dat',plot=True,ret=False,fit=False):
    """
    Plot and/or return cooling function.
    The 'cooling_function_Z0.dat' is read off Mo et al. (2010)'s Fig. 8.1,
    which is based on data from Sutherland & Dopita (1993).
    """
    T,L = np.loadtxt(file,unpack=True)
    T   = T * u.K
    L   = L * u.erg * u.cm**3 / u.s

    if plot:
        plt.clf()
        plt.xlim([1e4,1e8])
        plt.ylim([.2e-23,200e-23])
        plt.xlabel(r'$T \,/\, \mathrm{K}$',fontsize=14)
        plt.ylabel(r'$\Lambda \,/\, \mathrm{erg}\,\mathrm{cm}^3\,\mathrm{s}^{-1}$',fontsize=14)
        plt.xscale('log')
        plt.yscale('log')
        plt.plot(T,L,'-r',lw=2)

    if ret:
        return T,L
#------------------------------------------------------------------------------

def cooling_function_fit(T):
    """
    Fit for T > ~2e4 K from https://arxiv.org/pdf/1403.3076.pdf, eq. 6.
    The factor that is divided with in the end is a quick and dirty attempt to
    make it work at T < 2e4 K as well.
    """
    t = (T/u.K).value

    a = 4.86567e-13
    b = -2.21974
    c = 1.35332e-5
    d = 9.64775
    e = 1.11401e-9
    f = -2.66528
    g = 6.91908e-21
    h = -0.571255
    i = 2.45596e-27
    j = 0.49521

    atb = a * t**b
    ctd = (c*t)**d
    etf = e * t**f
    gth = g * t**h
    itj = i * t**j

    Lambda = (atb + ctd*(etf+gth)) / (1+ctd) + itj
    Lambda = Lambda / (1+1.0e5/(t-1.13e4)**1.4) # This could be improved significantly
    Lambda = Lambda * u.erg * u.cm**3 / u.s

    return Lambda
#------------------------------------------------------------------------------

def cooling_function_slow(T):
    t,l = cooling_function_from_file(plot=False,ret=True)
  # print('t    =', t[235],t[236])
  # print('l    =', l[235],l[236])
    i1  = np.searchsorted(t,T)
  # print('i0   =', i0)
    i0  = i1 - 1
  # print('i1   =', i1)
    dt0 = T - t[i0]
  # print('dt0  =', dt0)
  # dt1 = t[i1] - T
    dt  = t[i1] - t[i0]
  # print('dt   =', dt)
    dl  = l[i1] - l[i0]
  # print('dl   =', dl)
    L   = l[i0] + dt0/dt * dl
  # print('L    =', L)
    return L
#------------------------------------------------------------------------------

def cooling_time(n,T):
    """
    Compare t_cool with t_dyn in a density vs. temperature plot.
    """
    Lambda = cooling_function_fit(T)
    nH     = 12/27 * n
    num    = 3 * n * kB * T
    den    = 2 * nH**2 * Lambda
    return (num/den).to(u.Gyr)
#------------------------------------------------------------------------------

def halo_cooling(file='cooling_function_Z0.dat',fit=None,Delta=200):
    """
    Compare t_cool with t_dyn in a density vs. temperature plot.
    """
    if file:
        T,L = np.loadtxt(file,unpack=True)
        T   = T * u.K
        L   = L * u.erg * u.cm**3 / u.s
    else:
        T = np.logspace(3,8,501) * u.K
        L = cooling_function_fit(T)

    fb = .15
    mu = .59

    f1 = 59049/1024 * 32/(3*pi)
    f2 = G*mu*mH*kB**2 / fb
    n  = (f1*f2 * T**2 / L**2).to(u.cm**-3)

    def nm(M,T,Delta):
        f1 = 6/pi
        f2 = kB**3
        f3 = Delta * mu**4 * mH**4 * G**3
        return (f1 * f2/f3 * T**3 / M**2).to(u.cm**-3)

  # Mlines = np.arange(7,16) * u.Msun
  # nlines = np.array([nm(M,T,Delta) for M in Mlines])

    M07 = 1e07 * u.Msun
    M08 = 1e08 * u.Msun
    M09 = 1e09 * u.Msun
    M10 = 1e10 * u.Msun
    M11 = 1e11 * u.Msun
    M12 = 1e12 * u.Msun
    M13 = 1e13 * u.Msun
    M14 = 1e14 * u.Msun
    M15 = 1e15 * u.Msun
    M16 = 1e16 * u.Msun
    n07 = nm(M07,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n08 = nm(M08,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n09 = nm(M09,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n10 = nm(M10,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n11 = nm(M11,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n12 = nm(M12,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n13 = nm(M13,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n14 = nm(M14,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n15 = nm(M15,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?
    n16 = nm(M16,T,Delta) * 1/fb**4 # ARGH IS THIS CORRECT?

    nz0 = (cosmo.critical_density(0) * cosmo.Ob(0) / (mu*mH)).to(u.cm**-3).value * Delta
    nz1 = (cosmo.critical_density(1) * cosmo.Ob(1) / (mu*mH)).to(u.cm**-3).value * Delta
    nz2 = (cosmo.critical_density(2) * cosmo.Ob(2) / (mu*mH)).to(u.cm**-3).value * Delta
    nz3 = (cosmo.critical_density(3) * cosmo.Ob(3) / (mu*mH)).to(u.cm**-3).value * Delta
    nz4 = (cosmo.critical_density(4) * cosmo.Ob(4) / (mu*mH)).to(u.cm**-3).value * Delta
    nz5 = (cosmo.critical_density(5) * cosmo.Ob(5) / (mu*mH)).to(u.cm**-3).value * Delta
    nz10 = (cosmo.critical_density(10) * cosmo.Ob(10) / (mu*mH)).to(u.cm**-3).value * Delta

    plt.clf()
    plt.xlim([1e4,3e7])
    plt.ylim([1e-10,10])
    plt.xlabel(r'$T_\mathrm{vir} \,/\, \mathrm{K}$',fontsize=14)
    plt.ylabel(r'$n \,/\, \mathrm{cm}^{-3}$',fontsize=14)
    plt.xscale('log')
    plt.yscale('log')

    plt.fill_between(T.value,n.value,n.value*1e66,color='lime',alpha=.25)
    plt.fill_between(T.value,n.value,n.value/1e66,color='r',   alpha=.25)

    plt.plot(T,n,'-k',lw=2)

  # plt.plot(T,n07,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n08,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n09,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n10,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n11,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n12,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n13,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n14,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n15,'k',ls='--',dashes=(7, 5),lw=1)
    plt.plot(T,n16,'k',ls='--',dashes=(7, 5),lw=1)

    angle = 40
    plt.text(1e4,1.4e-3,r'$10^{10}\,M_\odot$',rotation=angle,fontsize='small')
    plt.text(3e4,3.4e-4,r'$10^{11}\,M_\odot$',rotation=angle,fontsize='small')
    plt.text(1e5,1.4e-4,r'$10^{12}\,M_\odot$',rotation=angle,fontsize='small')
    plt.text(3e5,3.4e-5,r'$10^{13}\,M_\odot$',rotation=angle,fontsize='small')
    plt.text(1e6,1.4e-5,r'$10^{14}\,M_\odot$',rotation=angle,fontsize='small')
    plt.text(3e6,3.4e-6,r'$10^{15}\,M_\odot$',rotation=angle,fontsize='small')
    plt.text(1e7,1.4e-6,r'$10^{16}\,M_\odot$',rotation=angle,fontsize='small')

    plt.plot([T.value[0],T.value[-1]], [nz0,nz0],'b-',lw=.5)
    plt.plot([T.value[0],T.value[-1]], [nz1,nz1],'b-',lw=.5)
  # plt.plot([T.value[0],T.value[-1]], [nz2,nz2],'b-',lw=.5)
    plt.plot([T.value[0],T.value[-1]], [nz3,nz3],'b-',lw=.5)
  # plt.plot([T.value[0],T.value[-1]], [nz4,nz4],'b-',lw=.5)
  # plt.plot([T.value[0],T.value[-1]], [nz5,nz5],'b-',lw=.5)
    plt.plot([T.value[0],T.value[-1]], [nz10,nz10],'b-',lw=.5)

    plt.text(1e7,1.1*nz0, r'$z = 0$', color='b',fontsize='small')
    plt.text(1e7,1.1*nz1, r'$z = 1$', color='b',fontsize='small')
    plt.text(1e7,1.1*nz3, r'$z = 3$', color='b',fontsize='small')
    plt.text(1e7,1.1*nz10,r'$z = 10$',color='b',fontsize='small')
#------------------------------------------------------------------------------

def freefall_timescale(z,Delta=200,cosmo=Planck18):
  # fbar = cosmo.Ob(z) / cosmo.Om(z)
  # rhom = Delta * cosmo.critical_density(z) * cosmo.Om(z)
  # tff  = (3*pi / (32*G*rhom))**(1/2)
    #Mo+ 10:
    fgas = 0.15
    nm3  = 1.9e-2 * fgas * (1+Delta) * (cosmo.Om0*cosmo.h**2) * (1+z)**3 # n_{-3} = n / 1e3 cm**-3
    tff  = 2.1 * sqrt(fgas/nm3) * u.Gyr
    return tff#.to(u.Gyr)
#------------------------------------------------------------------------------

def hmf2smf(cosmo=Planck18):
    h    = cosmo.h
  # h = .7
    invh = 1 / h
    ln10 = np.log(10)

    logMlo = 6.
    logMhi = 16.
    Mlo    = 10**logMlo
    Mhi    = 10**logMhi
    n      = 1001
    hM     = np.logspace(logMlo,logMhi,n) # M / Mo/h
    h3HMF  = dNdlnM(hM, 0.1)              # dN/dlnM / h-3 Mpc-3
    M      = hM     * invh
    HMF    = h3HMF  * invh**3 / ln10

    rhob0 = cosmo.critical_density0 * cosmo.Ob0
    rhom0 = cosmo.critical_density0 * cosmo.Om0
    fb    = rhob0 / rhom0

    Ms_wr, n_wr,nlo_wr,nhi_wr = np.loadtxt('wright2017_SMF_z0.1.dat',unpack=True)
    Ms_ba, n_ba,nlo_ba,nhi_ba = np.loadtxt('bernardi2013_SMF_z0.1.dat',unpack=True)
    Ms_go, n_go               = np.loadtxt('gonzalez-perez_2014.dat',unpack=True)
    Ms_cr, n_cr               = np.loadtxt('croton_2016.dat',unpack=True)
    Ms_vo, n_vo               = np.loadtxt('vogelsberger_2015.dat',unpack=True)
    Ms_sc, n_sc               = np.loadtxt('schaye_2014.dat',unpack=True)
  # n_ba,nlo_ba,nhi_ba = ln10*n_ba,ln10*nlo_ba,ln10*nhi_ba

    fs = 14
    plt.clf()
    plt.xlim([Mlo,Mhi])
    plt.ylim([1e-6,1e2])
  # plt.xlabel(r'$M_{\mathrm{h}}/h^{-1}M_\odot$',fontsize=fs)
  # plt.ylabel(r'$dN/d\ln M\,\,/\,\,h^3\mathrm{Mpc}^{-3}$',fontsize=fs)
    plt.xlabel(r'$M \, / \, M_\odot$',fontsize=fs)
    plt.ylabel(r'$dN/d\log M\,\,/\,\,\mathrm{Mpc}^{-3}$',fontsize=fs)
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(M,HMF, 'b-',lw=2,label=r'$\mathrm{HMF: } N(M_\mathrm{h})$')
    plt.plot(M*fb,HMF,'fuchsia',ls='-',lw=2,label=r'$\mathrm{HMF: } N(M_\mathrm{h} \times f_\mathrm{b})$')

    plt.errorbar(Ms_wr,n_wr, yerr=[n_wr-nlo_wr,nhi_wr-n_wr],capsize=2,ecolor='olive',fmt='none',mec='olive', alpha=.5)          #Indiv. gal error bars
    plt.scatter(Ms_wr,n_wr,color='olive',s=20,zorder=9,label='SMF: Observed (Wright+ 2017)')
    plt.errorbar(Ms_ba,n_ba, yerr=[n_ba-nlo_ba,nhi_ba-n_ba],capsize=2,ecolor='steelblue',fmt='none',mec='steelblue', alpha=.5)          #Indiv. gal error bars
    plt.scatter(Ms_ba,n_ba,color='steelblue',s=20,zorder=9,label='SMF: Observed (Bernardi+ 2013)')

    plt.plot(Ms_go,n_go,c='saddlebrown',ls='-', lw=1,zorder=10,label='SMF: Semi-analytical (GALFORM)')
    plt.plot(Ms_cr,n_cr,c='saddlebrown',ls='--',lw=1,zorder=10,label='SMF: Semi-analytical (SAGE)')
    plt.plot(Ms_vo,n_vo,c='darkturquoise',   ls='-', lw=1,zorder=10,label='SMF: Numerical (Illustris)')
    plt.plot(Ms_sc,n_sc,c='darkturquoise',   ls='--',lw=1,zorder=10,label='SMF: Numerical (EAGLE)')

    plt.annotate('', xy=(1.4e10,2.36e-2),  # arrowhead coords
            xytext=(1.2e11,2.36e-2),                 # text coords
            va='center',
            ha='center',
            arrowprops=dict(
                color='k',
                alpha=.8,
                lw=5,
                capstyle='butt',
                joinstyle='miter',
                arrowstyle='->',              # Also '->', '-[', '<|-|>', etc.
                connectionstyle='arc3'         # 'arc3' is a straight arrow. Other styles are 'angle', 'angle3', 'bar', etc.
                )
            )

  # plt.annotate('', xy=(1e7,1e-1),  # arrowhead coords
  #         xytext=(1e9,1),                 # text coords
  #         va='center',
  #         ha='center',
  #         arrowprops=dict(
  #             color='lime',
  #             alpha=.25,
  #             lw=10,
  #             capstyle='butt',
  #             joinstyle='miter',
  #             arrowstyle='->',              # Also '->', '-[', '<|-|>', etc.
  #             connectionstyle='arc3,rad=.3'         # 'arc3' is a straight arrow. Other styles are 'angle', 'angle3', 'bar', etc.
  #             )
  #         )

  # style = "Simple, tail_width=0.5, head_width=4, head_length=8"
  # kw = dict(arrowstyle=style, color="k")
  # patches.FancyArrowPatch((1e9,1), (1e7,1e-1),
  #         connectionstyle="arc3,rad=.5")#, **kw)

    plt.legend(scatterpoints=1)
#------------------------------------------------------------------------------
