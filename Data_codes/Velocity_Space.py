"""
@author: %(Setareh Foroozan)
"""
#colormap is velocity

import h5py
f = h5py.File('groups_048.0.hdf5', 'r')

head_subhalo = f['Subhalo']
SubhaloPos = head_subhalo['SubhaloPos']
SubhaloVel = head_subhalo['SubhaloVel']

X_SubhaloPos = SubhaloPos[:,0] / 1000
Y_SubhaloPos = SubhaloPos[:,1] / 1000
Z_SubhaloPos = SubhaloPos[:,2] / 1000
X_SubhaloVel = SubhaloVel[:,0]
Y_SubhaloVel = SubhaloVel[:,1]
Z_SubhaloVel = SubhaloVel[:,2]
V_Subhalo = (X_SubhaloVel ** 2 + Y_SubhaloVel ** 2 + Z_SubhaloVel ** 2) ** (1/2)

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

# load some test data for demonstration and plot a wireframe
title = 'Velocity_Histogram'
plt.title(title)
sc = plt.scatter(X_SubhaloPos, Y_SubhaloPos, c = V_Subhalo, s = 1 ,edgecolors = 'none', cmap = 'hot')
cb = plt.colorbar(sc)
cb.set_label('Velocity')
cb.set_clim([min(V_Subhalo),max(V_Subhalo)])
plt.xlabel('X(10^3)')
plt.ylabel('Y(10^3)')
plt.savefig('{}.png'.format(title))
plt.show()
