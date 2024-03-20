import os

import numpy as np
import cv2

rgb_path = "/home/lc/SplaTAM/data/TUM_RGBD/rgbd_dataset_freiburg3_walking_xyz_modified/rgb"
mask_path = "/home/lc/SplaTAM/data/TUM_RGBD/rgbd_dataset_freiburg3_walking_xyz_modified/mask"
rgb_mask_path = "/home/lc/SplaTAM/data/TUM_RGBD/rgbd_dataset_freiburg3_walking_xyz_modified/rgb_mask"
img_list = os.listdir(rgb_path)
mask_list = os.listdir(mask_path)

for file in range(0,len(img_list)):

    img = cv2.imread(os.path.join(rgb_path,img_list[file]))
    mask = cv2.imread(os.path.join(mask_path,mask_list[file]))
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    background = np.zeros_like(img)

    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask_3[i,j] !=0:
                img[i,j] = background[i,j]
    print(img)
    cv2.imwrite(os.path.join(rgb_mask_path,img_list[file]),img)
    print(img_list[file])