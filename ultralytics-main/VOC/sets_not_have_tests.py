# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#进行验证数据的选取
# ************************************************************************************************

import os, random, shutil


def moveimg(fileDir, tarDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.1  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    for name in sample:
        shutil.move(fileDir + name, tarDir + "\\" + name)
    return


def movelabel(file_list, file_label_train, file_label_val):
    for i in file_list:
        if i.endswith('.jpg'):
            filename = file_label_train + "\\" + i[:-4] + '.txt'  # 可以改成xml文件将’.txt‘改成'.xml'就可以了
           # filename = file_label_train + "\\" + i[:-4] + '.json'  # 可以改成xml文件将’.txt‘改成'.xml'就可以了
            if os.path.exists(filename):
                shutil.move(filename, file_label_val)
                print(i + "处理成功！")


if __name__ == '__main__':
    fileDir = r"E:\anewshen\ultralytics-main\ultralytics-main\VOC\VOC\images\train" + "\\"  # 源图片文件夹路径
    tarDir = r"E:\anewshen\ultralytics-main\ultralytics-main\VOC\VOC\images\val"  # 图片移动到新的文件夹路径
    moveimg(fileDir, tarDir)
    file_list = os.listdir(tarDir)
    file_label_train = r"E:\anewshen\ultralytics-main\ultralytics-main\VOC\VOC\labels\train"  # 源图片标签路径
    file_label_val = r"E:\anewshen\ultralytics-main\ultralytics-main\VOC\VOC\labels\val"  # 标签
    # 移动到新的文件路径
    movelabel(file_list, file_label_train, file_label_val)

# *********************************************************************************************************









































# '''
# 一个划分数据集，->没有测试集文件<-的脚本
# '''
# import shutil
# import random
# import os
#
# # 原始图像和标签的路径
# image_original_path = r"E:\anewshen\ultralytics-main\ultralytics-main\123\im"
# label_original_path = r"E:\anewshen\ultralytics-main\ultralytics-main\123\la"
# cur_path = os.getcwd()
# print("cur_path:", cur_path)
#
# # 训练集图像和标签的路径
# train_image_path = os.path.join(cur_path, r"VOC\images\train")
# train_label_path = os.path.join(cur_path, r"VOC\labels\train")
#
# # 验证集图像和标签的路径
# val_image_path = os.path.join(cur_path, r"VOC\images\val")
# val_label_path = os.path.join(cur_path, r"VOC\labels\val")
#
# # 训练集目录
# list_train = os.path.join(cur_path, "VOC/images/train.txt")
# list_val = os.path.join(cur_path, "VOC/labels/val.txt")
#
# train_percent = 0.8  # 训练集所占比例
# val_percent = 0.2  # 验证集所占比例
#
#
# def del_file(path):
#     for i in os.listdir(path):
#         file_data = path + "\\" + i
#         os.remove(file_data)
#
#
# def mkdir():
#     if not os.path.exists(train_image_path):
#         os.makedirs(train_image_path)
#     else:
#         del_file(train_image_path)
#     if not os.path.exists(train_label_path):
#         os.makedirs(train_label_path)
#     else:
#         del_file(train_label_path)
#     if not os.path.exists(val_image_path):
#         os.makedirs(val_image_path)
#     else:
#         del_file(val_image_path)
#     if not os.path.exists(val_label_path):
#         os.makedirs(val_label_path)
#     else:
#         del_file(val_label_path)
#
#
# def clearfile():
#     if os.path.exists(list_train):
#         os.remove(list_train)
#     if os.path.exists(list_val):
#         os.remove(list_val)
#
#
# def main():
#     mkdir()
#     clearfile()
#     file_train = open(list_train, 'w')
#     file_val = open(list_val, 'w')
#     total_txt = os.listdir(label_original_path)
#     num_txt = len(total_txt)
#     list_all_txt = range(num_txt)
#     num_train = int(num_txt * train_percent)
#     # 随机选取训练集数据
#     train = random.sample(list_all_txt, num_train)
#     for i in list_all_txt:
#         if i in train:
#             # 将图片和标签复制到训练集文件夹
#             shutil.copy(os.path.join(image_original_path, total_txt[i]), train_image_path)
#             shutil.copy(os.path.join(label_original_path, total_txt[i]), train_label_path)
#             file_train.write(os.path.join(train_image_path, total_txt[i]) + '\n')
#         else:
#             # 将图片和标签复制到验证集文件夹
#             shutil.copy(os.path.join(image_original_path, total_txt[i]), val_image_path)
#             shutil.copy(os.path.join(label_original_path, total_txt[i]), val_label_path)
#             file_val.write(os.path.join(val_image_path, total_txt[i]) + '\n')
#     file_train.close()
#     file_val.close()
#
# try:
#     shutil.copy(os.path.join(image_original_path, label_original_path), train_image_path)
# except FileNotFoundError as e:
#     print(f"源文件不存在: {e}")
# except PermissionError as e:
#     print(f"权限不足: {e}")
# except Exception as e:
#     print(f"其他文件操作错误: {e}")
#
# if __name__ == '__main__':
#     main()
