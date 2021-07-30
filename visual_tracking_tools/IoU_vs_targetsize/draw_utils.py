import numpy as np
from os.path import join

COLOR = ((1, 0, 0),
         (0, 1, 0),
         (1, 0, 1),
         (1, 1, 0),
         (0  , 162/255, 232/255),
         (0.5, 0.5, 0.5),
         (0, 0, 1),
         (0, 1, 1),
         (136/255, 0  , 21/255),
         (255/255, 127/255, 39/255),
         (0, 0, 0),
         (0  , 142/255, 232/255),
         (225/255, 127/255, 239/255),
         (15/255, 127/255, 219/255),
         (205/255, 127/255, 39/255),
         (105/255, 22/255, 139/255),
         (180/255, 227/255, 179/255),
         )

LINE_STYLE = ['-', '-', '-', '-', '-', '--', '-', '--', '-', '--', '-', ':', ':', ':', ':',':']

MARKER_STYLE = ['o', 'v', '<', '*', 'D', 'x', '.', 'x', '<', '.']


# Compute IoU @PySOT
def overlap_ratio(rect1, rect2):
    '''Compute overlap ratio between two rects
    Args
        rect:2d array of N x [x,y,w,h]
    Return:
        iou
    '''
    left = np.maximum(rect1[0], rect2[0])
    right = np.minimum(rect1[0]+rect1[2], rect2[0]+rect2[2])
    top = np.maximum(rect1[1], rect2[1])
    bottom = np.minimum(rect1[1]+rect1[3], rect2[1]+rect2[3])

    intersect = np.maximum(0,right - left) * np.maximum(0,bottom - top)
    union = rect1[2]*rect1[3] + rect2[2]*rect2[3] - intersect
    iou = intersect / union
    iou = np.maximum(np.minimum(1, iou), 0)
    return iou


# Read tracker results
def read_results(result_base_path, video_name, trackers):
    results_raw = {}
    for tracker in trackers:
        result_path = join(result_base_path, tracker, video_name) + '.txt'
        with open(result_path, 'r') as f:
            results_raw[tracker] = f.readlines()
        f.close()
    return results_raw

