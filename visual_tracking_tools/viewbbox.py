import sys
import os
sys.path.append(os.getcwd())
sys.path.append('/home/lyz/pysot-toolkit-master')
from pysot.datasets import DatasetFactory
from pysot.utils.region import vot_overlap
import numpy as np
import os
import cv2
from os.path import join
def x1y1wh2x1y1x2y2(bbox):
    return [int(float(bbox[0])), int(float(bbox[1])), int(float(bbox[0]) + float(bbox[2])), int(float(bbox[1]) + float(bbox[3]))]

#init
trackers=[]

trackers.append('BACF')
trackers.append('HDT')
trackers.append('SiamFC')
trackers.append('MDNet')
trackers.append('SRDCF')
trackers.append('DSST')
trackers.append('Staple')
trackers.append('KCF')
trackers.append('DCDA')
# load results
result_base_path = '/home/lyz/results/Compare/NFS30'


#load dataset
otb_root = '/home/lyz/NFSDataset'
dataset = DatasetFactory.create_dataset(name = 'NFS30', dataset_root = otb_root, load_img = False)

COLOR = [(0, 1, 0),
         (1, 0, 1),
         (1, 1, 0),
         (0  , 162/255, 232/255),
         (0.5, 0.5, 0.5),
         (0, 0.8, 0.4),
         (0, 0, 0),
         (180/255, 227/255, 179/255),
         (0, 0, 1)
         # (255/255, 127/255, 39/255),
         # (0, 0, 0),
         # (0  , 142/255, 232/255),
         # (225/255, 127/255, 239/255),
         # (15/255, 127/255, 219/255),
         # (205/255, 127/255, 39/255),
         # (105/255, 22/255, 139/255),
         # (180/255, 227/255, 179/255),
         ]

for video in dataset:
    if video.name != 'shuffleboard_2':
       continue
    tracker_path = []
    for tk in trackers:
        tracker_path.append(join(result_base_path, tk, video.name) +'.txt')

    print('video:',video.name)
    for idx, img_path in enumerate(video.img_names):
        print(idx)
        showimg = cv2.imread(img_path)
        # showimg = cv2.cvtColor(showimg, cv2.COLOR_BGR2RGB)
        for i, tk in enumerate(tracker_path):
            with open(tk, 'r') as f:
                tmp = f.readlines()[idx]
                tmpbox = [tmp.split(',')[0], tmp.split(',')[1], tmp.split(',')[2], tmp.split(',')[3].split()[0]]
                showbox = x1y1wh2x1y1x2y2(tmpbox)
                cv2.rectangle(showimg, (showbox[0], showbox[1]), (showbox[2], showbox[3]), (COLOR[i][0]*255, COLOR[i][1]*255, COLOR[i][2]*255), thickness=4)
                # cv2.line(showimg, (10+ i *10 ,0), (10 + i *10, 200), (COLOR[i][0]*255, COLOR[i][1]*255, COLOR[i][2]*255), thickness=5)
                # showimg = cv2.cvtColor(showimg, cv2.COLOR_RGB2BGR)
                f.close()
        cv2.imshow('FF', showimg)
        cv2.imwrite('NFS_30_'+video.name+'.png',showimg)
        cv2.waitKey(0)