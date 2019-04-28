"""
@author: %(Setareh Foroozan
This code will save only the positions of SUBHALOS from illustris-3 at Z = 0
"""
import h5py
import numpy as np
#reading hdf file
N_docs = 2
X_SubhaloPos = np.array([])
Y_SubhaloPos = np.array([])
Z_SubhaloPos = np.array([])
for i in range(N_docs):
    f = h5py.File('/Users/apple/Desktop/groups_135.{}.hdf5'.format(i), 'r')
    head_snap = f['Subhalo']
    DMPos = head_snap['SubhaloPos']
    X_SubhaloPos = np.concatenate((X_SubhaloPos, DMPos[:,0]), axis = 0)
    Y_SubhaloPos = np.concatenate((Y_SubhaloPos, DMPos[:,1]), axis = 0)
    Z_SubhaloPos = np.concatenate((Z_SubhaloPos, DMPos[:,2]), axis = 0)
np.save('X_SubhaloPos', X_SubhaloPos)
np.save('Y_SubhaloPos', Y_SubhaloPos)
np.save('Z_SubhaloPos', Z_SubhaloPos)
