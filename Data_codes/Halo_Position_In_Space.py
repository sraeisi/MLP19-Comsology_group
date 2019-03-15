"""
@author: %(Setareh Foroozan)
"""
#Halo distribution in space
import h5py
#reading hdf file
f = h5py.File('groups_048.0.hdf5', 'r')
head_subhalo = f['Subhalo']
SubhaloPos = head_subhalo['SubhaloPos']
X_SubhaloPos = SubhaloPos[:,0] / 1000
Y_SubhaloPos = SubhaloPos[:,1] / 1000
Z_SubhaloPos = SubhaloPos[:,2] / 1000

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# load some test data for demonstration and plotting
title = 'Halo_distribution_in_space'
ax.set_title(title)
ax.scatter(X_SubhaloPos, Y_SubhaloPos, Z_SubhaloPos, s = 0.1, color = 'teal')
ax.set_xlabel('X(10^3)')
ax.set_ylabel('Y(10^3)')
ax.set_zlabel('Z(10^3)')
fig.savefig('{}.png'.format(title))
plt.show()
