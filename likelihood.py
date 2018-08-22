#!/usr/bin/env python

import numpy
from scipy.stats import poisson
from scipy.optimize import root
from scipy.optimize import fmin
from scipy.integrate import quad
import matplotlib.pyplot as plt


nobs = 19

ntry = numpy.arange(nobs*.6,nobs*1.6,nobs/6.)

percentile = 0.68

def like():
	plt.clf()
	chisq = -2*numpy.log(poisson.pmf(nobs, nobs))
	r2 = root(lambda x : -2*numpy.log(poisson.pmf(nobs,x))-(chisq+1),nobs*1.1).x[0]
	r1 = root(lambda x : -2*numpy.log(poisson.pmf(nobs,x))-(chisq+1),nobs*0.9).x[0]

	x = numpy.arange(1,40,.1)
	plt.plot(x, poisson.pmf(nobs, x),linewidth=2,color='black')
	plt.ylabel(r'$L(N; N_o)$')
	plt.xlabel(r'$N$')
	plt.axvline(x=r1,label=r"$N_{{low}}={:6.3f}$".format(r1),ls=':',linewidth=2,color='red')
	plt.axvline(x=r2,label=r"$N_{{high}}={:6.3f}$".format(r2),ls=':',linewidth=2,color='red')
	plt.axvline(x=nobs,label=r"$N_{{max}}={}$".format(nobs),ls=':',linewidth=2,color='blue')
	plt.axhline(y=poisson.pmf(nobs, nobs),label=r"$L_{{max}}$".format(nobs),ls=':',linewidth=2,color='green')
	plt.axhline(y=numpy.exp(-(chisq+1)/2),label=r"$-2\log{{L_{{max}}}}+\Delta \chi^2$".format(nobs),ls=':',linewidth=2,color='green')

	plt.legend(loc=2,fontsize='medium')
	plt.title(r'$-\Delta 2\log(L_{max}) + \Delta \chi^2$' )
	plt.savefig('like.pdf')

def freq():
	plt.clf()
	for n in ntry:
		r = poisson.interval(.68,n)
		plt.plot(r,(n,n),color='black',linewidth=2)


	nmax = root(lambda x : poisson.interval(.68,x)[1]-nobs,nobs*.8).x[0]
	plt.plot(poisson.interval(.68,nmax),(nmax,nmax),color='red',label=r"$N_{{low}} = {:6.3f}$".format(nmax),linewidth=2)
	nmin = root(lambda x : poisson.interval(.68,x)[0]-nobs,nobs*1.2).x[0]

	plt.plot(poisson.interval(.68,nmin),(nmin,nmin),color='red',label=r"$N_{{high}} = {:6.3f}$".format(nmin),linewidth=2)

	plt.plot(poisson.interval(.68,nobs),(nobs,nobs),color='blue',label=r"$N_{{max}} = {}$".format(nobs),linewidth=2)


	plt.axvline(x=nobs,label=r"$N_{{o}}={}$".format(nobs),ls=':',linewidth=2)
	plt.xlabel(r'68%  $N_o$ range')
	plt.ylabel(r'$N$')
	plt.legend(loc=0)
	plt.title(r'frequentist' )
	plt.savefig('freq.pdf')

def f(l):
	r2 = root(lambda x : poisson.pmf(nobs,x)-l,nobs*1.1).x[0]
	r1 = root(lambda x : poisson.pmf(nobs,x)-l,nobs*0.9).x[0]
	area = quad(lambda x : poisson.pmf(nobs,x),r1,r2)[0]
	print l, r1, r2, area
	return area-0.68

def posterior():
	plt.clf()
	# print (quad(lambda x : poisson.pmf(nobs,x),0,numpy.inf)[0])
	ans=0.05533

	r2 = root(lambda x : poisson.pmf(nobs,x)-ans,nobs*1.1).x[0]
	r1 = root(lambda x : poisson.pmf(nobs,x)-ans,nobs*0.9).x[0]	
	f(ans)
	x = numpy.arange(1,40,.1)
	plt.plot(x, poisson.pmf(nobs, x),linewidth=2,color='black')
	plt.ylabel(r'$p(N|N_o)$')
	plt.xlabel(r'$N$')
	plt.axvline(x=r1,label=r"$N_{{low}}={:6.3f}$".format(r1),ls=':',linewidth=2,color='red')
	plt.axvline(x=r2,label=r"$N_{{high}}={:6.3f}$".format(r2),ls=':',linewidth=2,color='red')
	plt.axvline(x=nobs,label=r"$N_{{max}}={}$".format(nobs),ls=':',linewidth=2,color='blue')
	plt.legend(loc=2,fontsize='medium')
	plt.title(r'credible interval' )
	plt.savefig('post.pdf')

freq()
# like()
# posterior()