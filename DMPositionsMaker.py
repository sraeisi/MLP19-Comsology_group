"""
@author: %(Setareh Foroozan
This code will save only the positions of DM from illustris-3 at Z = 0
"""
import h5py
import numpy as np
#reading hdf file
N_docs = 32
X_DMPos = np.array([])
Y_DMPos = np.array([])
Z_DMPos = np.array([])
for i in range(N_docs):
    f = h5py.File('/Volumes/setare/Illustris/snap_135.{}.hdf5'.format(i), 'r')
    head_snap = f['PartType1']
    DMPos = head_snap['Coordinates']
    X_DMPos = np.concatenate((X_DMPos, DMPos[:,0]), axis = 0)
    Y_DMPos = np.concatenate((Y_DMPos, DMPos[:,1]), axis = 0)
    Z_DMPos = np.concatenate((Z_DMPos, DMPos[:,2]), axis = 0)
np.save('X_DMPos', X_DMPos)
np.save('Y_DMPos', Y_DMPos)
np.save('Z_DMPos', Z_DMPos)
