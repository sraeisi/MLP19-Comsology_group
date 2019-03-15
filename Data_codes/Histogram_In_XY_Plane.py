"""
@author: %(Setareh Foroozan)
"""
#Halo distribution in space

import h5py
f = h5py.File('groups_048.0.hdf5', 'r')

head_subhalo = f['Subhalo']
SubhaloPos = head_subhalo['SubhaloPos']

X_SubhaloPos = SubhaloPos[:,0] / 1000
Y_SubhaloPos = SubhaloPos[:,1] / 1000

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# load some test data for demonstration and plot a wireframe
title = 'Histogram_In_XY_Plane'
ax.set_title(title)
ax.hist2d(X_SubhaloPos, Y_SubhaloPos, bins = 300, cmap = 'hot')
ax.set_xlabel('X(10^3)')
ax.set_ylabel('Y(10^3)')
fig.savefig('{}.png'.format(title))
plt.show()
