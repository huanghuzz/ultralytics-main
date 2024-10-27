'''
一个划分数据集，->没有测试集文件<-的脚本
'''
import shutil
import random
import os

# 原始图像和标签的路径
image_original_path = "E:/anewshen/ultralytics-main/ultralytics-main\VOC/voc\im"
label_original_path = "E:/anewshen/ultralytics-main/ultralytics-main\VOC/voc\la"
cur_path = os.getcwd()

# 训练集图像和标签的路径
train_image_path = os.path.join(cur_path,"E:/anewshen/ultralytics-main/ultralytics-main/VOC/images/train")
train_label_path = os.path.join(cur_path, "E:/anewshen/ultralytics-main/ultralytics-main/VOC/labels/train")

# 验证集图像和标签的路径
val_image_path = os.path.join(cur_path, "E:/anewshen/ultralytics-main/ultralytics-main/VOC/images/val")
val_label_path = os.path.join(cur_path, "E:/anewshen/ultralytics-main/ultralytics-main/VOC/labels/val")

# 训练集目录
list_train = os.path.join(cur_path, "VOC/images/train.txt")
list_val = os.path.join(cur_path, "VOC/labels/val.txt")

train_percent = 0.8  # 训练集所占比例
val_percent = 0.2  # 验证集所占比例

def del_file(path):
    for i in os.listdir(path):
        file_data = path + "\\" + i
        os.remove(file_data)

def mkdir():
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path)
    else:
        del_file(train_image_path)
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path)
    else:
        del_file(train_label_path)
    if not os.path.exists(val_image_path):
        os.makedirs(val_image_path)
    else:
        del_file(val_image_path)
    if not os.path.exists(val_label_path):
        os.makedirs(val_label_path)
    else:
        del_file(val_label_path)

def clearfile():
    if os.path.exists(list_train):
        os.remove(list_train)
    if os.path.exists(list_val):
        os.remove(list_val)

def main():
    mkdir()
    clearfile()
    file_train = open(list_train, 'w')
    file_val = open(list_val, 'w')
    total_txt = os.listdir(label_original_path)
    num_txt = len(total_txt)
    list_all_txt = range(num_txt)
    num_train = int(num_txt * train_percent)
    # 随机选取训练集数据
    train = random.sample(list_all_txt, num_train)
    for i in list_all_txt:
        if i in train:
            # 将图片和标签复制到训练集文件夹
            shutil.copy(os.path.join(image_original_path, total_txt[i]), train_image_path)
            shutil.copy(os.path.join(label_original_path, total_txt[i]), train_label_path)
            file_train.write(os.path.join(train_image_path, total_txt[i]) + '\n')
        else:
            # 将图片和标签复制到验证集文件夹
            shutil.copy(os.path.join(image_original_path, total_txt[i]), val_image_path)
            shutil.copy(os.path.join(label_original_path, total_txt[i]), val_label_path)
            file_val.write(os.path.join(val_image_path, total_txt[i]) + '\n')
    file_train.close()
    file_val.close()

if __name__ == '__main__':
    main()