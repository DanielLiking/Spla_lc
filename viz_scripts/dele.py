import os


# 指定文件夹路径
# folder_path = '/home/lc/SplaTAM/data/TUM_RGBD/rgbd_dataset_freiburg3_walking_xyz/depth'
#
# # 指定文件名列表
# file_names_list = os.listdir('/home/lc/SplaTAM/data/TUM_RGBD/rgbd_dataset_freiburg3_walking_xyz/mask')
#
# # 遍历文件夹中的所有文件
# for filename in os.listdir(folder_path):
#     # 检查文件名是否在列表中
#     if filename not in file_names_list:
#         # 构建文件的完整路径
#         file_path = os.path.join(folder_path, filename)
#         # 删除文件
#         os.remove(file_path)
#         print(f'Deleted: {file_path}')

# 打开文本文件并读取内容
list = []
with open('/home/lc/SplaTAM/data/TUM_RGBD/rgbd_dataset_freiburg3_walking_xyz/b.txt', 'r') as file:
    lines = file.readlines()

# 遍历每一行
for line in lines:
    # 检查行是否包含特定的标记，例如"depth/"
    if "depth/" in line:
        # 使用split方法分割行，并获取包含"depth/"后的部分
        parts = line.split("depth/")
        # 获取深度图像文件名，即"depth/"后的部分
        depth_image_filename = parts[1].split()[0]
        list.append(depth_image_filename)
folder_path = '/home/lc/SplaTAM/data/TUM_RGBD/rgbd_dataset_freiburg3_walking_xyz/depth'
for filename in os.listdir(folder_path):
    # 检查文件名是否在列表中
    if filename not in list:
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, filename)
        # 删除文件
        os.remove(file_path)
        print(f'Deleted: {file_path}')
