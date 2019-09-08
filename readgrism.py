#!/usr/bin/env python3

#Created: Thu 29 Aug 2019
#Last Modified: 3 Sept 2019
#Author: Emma Clarke (emmaclar@andrew.cmu.edu)

#read Fortran output into Python
from scipy.io import FortranFile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
f = FortranFile('mb2grism.dat', 'r') #r=read-write mode

ng=1024

sky=[] #initialize
for i in range(0,ng,1):
    x=f.read_record('f4')
    sky.append(x)
f.close()

sky=np.transpose(sky)

plt.matshow(sky,fignum=None,cmap='PRGn',origin='lower')
plt.show()
###


#####
#written to output file: write(12) ng,blen,blenkms,pixa,pixm,zred,xpmin,xpmax
#ng
#blen=box size
#blenkms: blenkms=100.*blen*(1./(1.+zred))*sqrt(0.3*(1.+zred)**3.+0.7)
#pixa=((2000.-920.)*(1.+zred))/float(npixs) !pixel size in  observed angstroms
#pixm=blen/float(ng) !pixel size in comoving mpc/h:
#zred--> default value = 1.0
#xpmin=minval(sky)
#xpmax=maxval(sky)
#####

# ng=1024 blen=100.000000 blenkms=8803.40918 pixa=21.6000004 pixm=9.76562500E-02
# zred=1.00000000 xpmin=3.47672696E-31 xpmax=2.04984952E-26
