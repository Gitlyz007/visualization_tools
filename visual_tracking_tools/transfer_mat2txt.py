from os.path import join, isdir
import os
import glob
import xml.etree.ElementTree as ET
import json
from os import listdir
import scipy.io as sio
import h5py
import numpy as np

js = {}
Tracker_base_path = '/home/lyz/results/Compare/ECO-HC/UAV123'
matfiles = sorted(listdir(Tracker_base_path))

for matf in matfiles:
    mat_path = join(Tracker_base_path, matf)
    if len(matf.split('_')) == 4:
        video_name = matf.split('_')[2]+'_' +matf.split('_')[3].split('.')[0]
        # tracker_name = matf.split('_')[-1].split('.')[0]
    else:
        print(matf)
        video_name = matf.split('_')[2].split('.')[0]
        # tracker_name = matf.split('_')[1].split('.')[0]
    # mat = sio.loadmat(mat_path)
    mat = h5py.File(mat_path)
    data = mat['results']
    dd = np.transpose((mat[data[0][0]]['res']).value)
    # raw_result = list(mat['results'][0][0][0][0][3])
    raw_result = dd
    tracker_name = 'ECO-HC'
    root_path = join(Tracker_base_path, 'Trans_UAV123')
    if not os.path.isdir(root_path):
        os.makedirs(root_path)
    savepath = os.path.join(root_path, tracker_name)
    if not os.path.isdir(savepath):
        os.makedirs(savepath)
    result_path = os.path.join(savepath, '{}.txt'.format(video_name))
    with open(result_path, 'w') as f:
        for x in raw_result:
                f.write(','.join([str(i) for i in x]) + '\n')
print('')