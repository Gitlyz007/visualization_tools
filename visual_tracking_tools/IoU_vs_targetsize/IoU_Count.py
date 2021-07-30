import sys
import os
sys.path.append(os.getcwd())
sys.path.append('/home/lyz/pysot-toolkit-master')
from pysot.datasets import DatasetFactory
# from pysot.utils.region import vot_overlap
import numpy as np
import os
import cv2
from os.path import join
import matplotlib.pyplot as plt
from draw_utils import COLOR, LINE_STYLE, overlap_ratio, read_results

# Results setting
result_base_path = '/home/lyz/DCDA_Rev/OTB-2015'
trackers = ['SiamFC','DaSiamRPN','SiamRPN']

# Load dataset
data_root = '/home/lyz/OTB100'
dataset = DatasetFactory.create_dataset(name = 'OTB100', dataset_root = data_root, load_img = False)

# Size setting
small_threshold = 20
small_size = small_threshold ** 2
size_thresholds = np.arange(0, 1.00 * small_size, 0.01 * small_size)

# Init eval
success = {}
frame_counts = {}
for tracker in trackers:
    success[tracker] = np.zeros(len(size_thresholds))
    frame_counts[tracker] = np.zeros(len(size_thresholds))

# Evaluate
for video in dataset:
    print(video.name)
    # Handle txts
    raw_results = read_results(result_base_path, video.name, trackers)

    for idx, gt_bbox in enumerate(video.gt_traj):
        gt_size = gt_bbox[2] * gt_bbox[3]
        for tracker in trackers:
            # Handle raw results
            pbox = raw_results[tracker][idx]
            pbox = [float(pbox.split(',')[0]), float(pbox.split(',')[1]), float(pbox.split(',')[2]), float(pbox.split(',')[3].split()[0])]
            # IoU
            curr_IoU = overlap_ratio(np.array(pbox), np.array(gt_bbox))
            # Threshold analyze
            for i in range(len(size_thresholds)):
                if gt_size < size_thresholds[i]:
                    success[tracker][i] += curr_IoU
                    frame_counts [tracker][i] += 1

for idx, tracker in enumerate(trackers):
    for i in range(len(size_thresholds)):
        success[tracker][i] = success[tracker][i] / (frame_counts [tracker][i] + 10e-7)
        # print('Mean IoU of ', size_thresholds[i], ':', success[tracker][i])
        # print('Size ', size_thresholds[i], ':', frame_counts [tracker][i])
    plt.plot(np.arange(0, 1.00 * small_threshold, 0.01 * small_threshold), success[tracker], label = tracker,
             color=COLOR[idx], linestyle=LINE_STYLE[idx], linewidth=2)

plt.legend(loc='lower right', labelspacing=0.2)
plt.xlabel('Target Size')
plt.xticks(np.arange(0, small_threshold * 1.2, small_threshold * 0.2))
plt.ylabel('Mean IoU')
plt.show()