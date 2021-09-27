import numpy as np
import urllib.request
import re
import sys
from astropy.cosmology import FlatLambdaCDM
from astropy import units as u

bolshoi = FlatLambdaCDM(H0=70., Om0=0.26) # Bolshoi

def grep(filename,pattern):
  dec = '\d+.\d+'                               #"Normal" float
  exp = '\d+.\d+e[+-]\d+'                       #Exponential notation
  f   = open(filename, 'r')
  for line in f:
    if re.search(pattern,line):
      s = re.search(exp,line)   #Extract float from string
      if s == None: s = re.search(dec,line)   #Extract float from string
      res = s.group()
      return float(res)
#------------------------------------------------------------------------------

def CVDriver(dx=62.095,dy=62.095,z=8.8,dz=.0999,N=1,cosmo=bolshoi):
  """
  Driver & Robotham (2010) cosmic variance, Eq. 4.
  dx,dy: Side lengths in arcmin
  z,dz:  Mean redshift and redshift thickness
  """
  dA = cosmo.angular_diameter_distance(z).to(u.Mpc).value
  sc = dA * np.pi/180./60   #Scale in Mpc/arcmin

  h  = cosmo.h
  A  = h/.7 * dx * sc * (1+z)                   #Dimensions A,B,C are given in
  B  = h/.7 * dy * sc * (1+z)                   # Mpc / ()
  Cp = h/.7 * cosmo.comoving_distance(z+dz/2.).to(u.Mpc).value
  Cm = h/.7 * cosmo.comoving_distance(z-dz/2.).to(u.Mpc).value
  C  = Cp - Cm

  t1 = 1 - .03*np.sqrt((A/B)-1)
  t2 = 219.7 - 52.4*np.log10(A*B*291.)
  t3 = 3.21 * np.log10(A*B*291.)**2
  t4 = np.sqrt(N*C/291.)

  V  = A*B*C / (h/.7)**3 * h**3                 #Return
  CV =  1e-2 * t1 * (t2+t3) / t4                #Eq 4. is in %, so multiply by 1e-2
  return V,CV
#------------------------------------------------------------------------------

def CVC(dx   = 62.095,  # Field size in arcmin, x
        dy   = 62.095,  # Field size in arcmin, y
        z    = 8.8,     # Mean redshift of filter
        dz   = 0.0999,  # Redshift interval covered by filter
        n    = 100,     # Intrinsic number of objects in pencil beam
        ff   = 1,       # Halo filling factor
        c    = 1,       # Completeness
        sig8 = 0.82,    #
        bias = 'ST',
        UltraVISTA = False,
        printURL   = False,
        pattern    = 'Cosmic variance'
        ):
  """
  Python wrapper for the online CosmicVarianceCalculator at
  http://casa.colorado.edu/~trenti/CosmicVariance.html, based on the paper
  Trenti & Stiavelli (2008), ApJ, 676, 767.

  EDIT 2020: The calculator is now at
  https://www.ph.unimelb.edu.au/~mtrenti/cvc/CosmicVariance.html

  The CosmicVarianceCalculator estimates the one sigma fractional uncertainty
  on the galaxy number counts for high-redshift surveys. It takes into account
  fluctuations in the counts due to large scale structure ("cosmic variance")
  as well as due to Poisson noise.  

  That is, the uncertainties are for a population of some sort with a total
  given number. The calculator calculates the number of halos above a certain
  size and in a volume defined by the keywords, and then returns the
  uncertainties.

  This wrapper works by constructing a URL from the given input, storing the
  result in a temporary file, grepping the floating number on the line in the
  temp file with the patterns given in the keyword 'pattern', and returning the
  results as a tuple.

  Usage:
  ------
    >>> import CosVar as cv
    >>> var1[,var2,...] = cv.CVC(keywords)

    Example for one of Lucia's <xi>m = 0.95 slices:
    >>> cv.CVC(dx=237, dy=237, z=6.9, dz=1.7/20, sig8=.8, pattern=['errtot','poisson','cosvar'], n=3052695/20)

  Input keywords (with defaults):
  -------------------------------
    dx:         Field size in arcmin, x                            (10)
    dy:         Field size in arcmin, y                            (10)
    z:          Mean redshift of filter                            (1)
    dz:         Redshift interval covered by filter                (0.01)
    n:          Intrinsic number of objects in pencil beam         (100)
    ff:         Halo filling factor                                (1)
    c:          Completeness                                       (1)
    sig8:       sigma_8; fluctuations on  8 Mpc/h scales           (0.82)
    bias:       'PS' for Press-Schechter or 'ST' for Sheth-Tormen  ('ST')
    UltraVISTA: Use UltraVISTA values                              (False)
    printURL:   Print constructed URL                              (False)
    pattern:    Possible value of 'pattern' are (with shortcuts):
                * 'Total fractional error'                         ('errtot')
                * 'Poisson uncertainty'                            ('poisson')
                * 'Cosmic variance' (DEFAULT) (std, NOT var)       ('cosvar')
                * 'Intrinsic Number Density for Galaxies'          ('ngal')
                * 'Intrinsic Number Density for Dark Matter Halos' ('nhalo')
                * 'Minimum DM halo mass [Msun/h]'                  ('Mmin')
                * 'Average Bias'                                   ('bias')
                * 'Bias @ Minimum DM halo mass'                    ('biasmin')
                * 'Dimension' (Doesn't work yet!)                  ('dim')
                * 'Total volume'                                   ('Vtot')
    More than one pattern can be given in a list.
  """
  #"""
  #Example (for the UltraVISTA field):
  #>>> M     = logspace(9,12)   # Define mass axis with M/(Msun/h) in [1e9,1e12]
  #>>> cumMF = calccumMF(M)     # Calculate cumulative HMF (example name)
  #>>> err   = empty_like(M)    # Array for the total error
  #>>> for m

# Fix 'pattern'
  if type(pattern) != list: pattern = [pattern]
  if 'errtot'    in pattern: pattern[pattern.index('errtot')]  = 'Total fractional error'
  if 'poisson'   in pattern: pattern[pattern.index('poisson')] = 'Poisson uncertainty'
  if 'cosvar'    in pattern: pattern[pattern.index('cosvar')]  = 'Cosmic variance'
  if 'ngal'      in pattern: pattern[pattern.index('ngal')]    = 'Intrinsic Number Density for Galaxies'
  if 'nhalo'     in pattern: pattern[pattern.index('nhalo')]   = 'Intrinsic Number Density for Dark Matter Halos'
  if 'Mmin'      in pattern: pattern[pattern.index('Mmin')]    = 'Minimum DM halo mass'
  if 'bias'      in pattern: pattern[pattern.index('bias')]    = 'Average Bias'
  if 'biasmin'   in pattern: pattern[pattern.index('biasmin')] = 'Bias @ Minimum DM halo mass'
  if 'dim'       in pattern: pattern[pattern.index('dim')]     = 'Dimension'
  if 'Vtot'      in pattern: pattern[pattern.index('Vtot')]    = 'Total volume'
  if 'Dimension' in pattern: raise AssertionError("Pattern 'Dimension' returns only x-dimension.")

# UltraVISTA values
  if UltraVISTA:
    dx   = 62.095
    dy   = 62.095
    z    = 8.80 #8.79
    dz   = 0.0999
    sig8 = 0.82
    bias = 'ST'

# Make URL
  URL = 'https://www.ph.unimelb.edu.au/cgi-bin/mtrenti/prova.cgi' \
      + '?SurveyAreaX%3D='  + str(dx)   \
      + '&SurveyAreaY%3D='  + str(dy)   \
      + '&meanz%3D='        + str(z)    \
      + '&Dz%3D='           + str(dz)   \
      + '&intnum%3D='       + str(n)    \
      + '&haloff%3D='       + str(ff)   \
      + '&completeness%3D=' + str(c)    \
      + '&Sigma8%3D='       + str(sig8) \
      + '&bias='            + str(bias)
  if printURL: print(URL)

  tempfile = 'FEgraVRAeggf43fgAg6423Gadfvt'
  open(tempfile,'wb').write(urllib.request.urlopen(URL).read())

  res = []
  for pat in pattern:
    res.append(grep(tempfile,pat))

  if None in res: raise AssertionError('NoneType returned. Check pattern for misspellings.')

  return tuple(res)
#------------------------------------------------------------------------------
