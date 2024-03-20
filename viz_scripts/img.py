import cv2
import matplotlib.pyplot as plt
import numpy as np
# 读取图片
image_path = "/home/lc/w_x/mask/1341846313.592026.png"


# 使用OpenCV读取图片
img = cv2.imread(image_path)

# 将图片转换为NumPy数组
np_img = np.array(img)*255
print(np_img.shape)
# 显示图片
plt.imshow(cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB))
plt.show()
