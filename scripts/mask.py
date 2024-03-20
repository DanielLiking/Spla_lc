import cv2
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

source = '/home/lc/DynaSLAM/data/mask/1341846341.269883.png'
img = Image.open(source)

# 将图片转换为NumPy数组
img_array = np.array(img)

# 将像素值乘以255
img_array_scaled = img_array * 255
print(img_array_scaled)
# 将结果转换回PIL图片对象
img_scaled = Image.fromarray(img_array_scaled.astype(np.uint8))

# 显示图片
img_scaled.show()

