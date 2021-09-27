from astropy.cosmology import Planck13
from astropy import units as u
from astropy.cosmology import z_at_value
import CosVar as cv

def cosvar_per_slice(nsources,
                     nslices = 1,         # Number of slices (1 to use full box)
                     cosmo   = Planck13,  # Cosmology
                     sig8    = 0.8,       # sigma_8
                     z       = 6.9,       # Redshift of box center
                     L       = 607*u.Mpc  # Side length of box
                     ):

    d      = cosmo.comoving_distance(z)
    zlo    = z_at_value(cosmo.comoving_distance,d-L/2) #\_Redshifts of
    zhi    = z_at_value(cosmo.comoving_distance,d+L/2) #/ box front/back
    dz     = zhi - zlo
    am_Mpc = cosmo.arcsec_per_kpc_comoving(z).to(u.arcmin/u.Mpc)# arcmin/Mpc
    dx     = (am_Mpc * L).value
    pattern= ['Total fractional error', 'Poisson uncertainty', 'Cosmic variance']
    cosvar = cv.CVC(dx=dx, dy=dx, z=z, dz=dz/nslices,
                    sig8=sig8,
                    pattern=pattern,
                    n=nsources/nslices)
    for i,p in enumerate(pattern):
        print(p, cosvar[i])
