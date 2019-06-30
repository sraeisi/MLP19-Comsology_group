"""
@author: %(Setareh Foroozan)
"""
#matallicity histogram in space
import h5py
import numpy as np
#reading hdf file
f = h5py.File('groups_048.0.hdf5', 'r')
head_subhalo = f['Subhalo']
SubhaloSFR = head_subhalo['SubhaloSFR'][:]
SubhaloMass = head_subhalo['SubhaloMass'][:]

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(np.log(SubhaloMass), np.log(SubhaloSFR), s = 0.1,)
# load some test data for demonstration and plotting
title = 'Star Formation Rate vs Halo Mass'
ax.set_title(title)
ax.set_xlabel('Log(M)')
ax.set_ylabel('log(Star Formation Rate)')
fig.savefig('{}.png'.format(title))
plt.show()
