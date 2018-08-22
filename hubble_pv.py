#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy
from astropy.cosmology import WMAP9 as cosmo

xr=(0.007,0.21)

zline = numpy.arange(xr[0],xr[1],0.001)
m_line = -19.5 + cosmo.distmod(zline).value

z_cosmo = numpy.arange(numpy.log(0.01),numpy.log(0.2),0.1)
z_cosmo=numpy.exp(z_cosmo)
m  = -19.5 + cosmo.distmod(z_cosmo).value

num=len(z_cosmo)
numpy.random.seed(1)
pv = numpy.random.normal(0, 1500.,num)/3e5

plt.plot(zline, m_line)
plt.scatter(z_cosmo,m,color='b',label=r'Cosmological $z$')

z_obs = (1+z_cosmo)*(1+pv)-1
plt.xscale("log", nonposx='clip')
plt.xlabel(r"$z$",fontsize=22)
plt.xlim(xr)
plt.ylabel("$m$",fontsize=22)
plt.legend(loc=2)
plt.savefig('hubble.pdf')

plt.scatter(z_obs,m, color='r', label=r'Observed $z$')
for zc_, m_, zo_ in zip(z_cosmo,m,z_obs):
    # plt.arrow(zc_,m_,numpy.log(zo_/zc_),0,length_includes_head=True,head_length=0.1)
    plt.annotate('', xy=(zo_, m_), xytext=(zc_, m_), arrowprops=dict(arrowstyle="->"))

plt.legend(loc=2)
plt.savefig('hubble_pv.pdf')
plt.clf()

plt.plot(zline, m_line)
plt.scatter(z_cosmo,m,color='b',label=r'Cosmological $z$')

z_obs = (1+z_cosmo)*(1+pv)-1
plt.xscale("log", nonposx='clip')
plt.xlabel(r"$z$",fontsize=22)
plt.xlim(xr)
plt.ylabel("$m$",fontsize=22)
plt.legend(loc=2)

plt.scatter(z_obs,m, color='r', label=r'Observed $z$')
m_pec   = -19.5 + cosmo.distmod(z_obs).value

for mp_, m_, zo_ in zip(m_pec,m,z_obs):
    # plt.arrow(zc_,m_,numpy.log(zo_/zc_),0,length_includes_head=True,head_length=0.1)
    plt.annotate('', xy=(zo_, mp_), xytext=(zo_, m_), arrowprops=dict(arrowstyle="->"))

plt.legend(loc=2)
plt.savefig('hubble_pm.pdf')