'''
一个划分数据集的脚本，->有测试集<-分为训练，验证，测试
'''
import shutil
import random
import os

# 原始路径
image_original_path = "data/images/"
label_original_path = "data/labels/"
cur_path = os.getcwd()

# 训练集路径
train_image_path = os.path.join(cur_path, "datasets/images/train/")
train_label_path = os.path.join(cur_path, "datasets/labels/train/")

# 验证集路径
val_image_path = os.path.join(cur_path, "datasets/images/val/")
val_label_path = os.path.join(cur_path, "datasets/labels/val/")

# 测试集路径
test_image_path = os.path.join(cur_path, "datasets/images/test/")
test_label_path = os.path.join(cur_path, "datasets/labels/test/")

# 训练集目录
list_train = os.path.join(cur_path, "datasets/train.txt")
list_val = os.path.join(cur_path, "datasets/val.txt")
list_test = os.path.join(cur_path, "datasets/test.txt")

train_percent = 0.8
val_percent = 0.1
test_percent = 0.1

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
    if not os.path.exists(test_image_path):
        os.makedirs(test_image_path)
    else:
        del_file(test_image_path)
    if not os.path.exists(test_label_path):
        os.makedirs(test_label_path)
    else:
        del_file(test_label_path)

def clearfile():
    if os.path.exists(list_train):
        os.remove(list_train)
    if os.path.exists(list_val):
        os.remove(list_val)
    if os.path.exists(list_test):
        os.remove(list_test)

def main():
    mkdir()
    clearfile()
    file_train = open(list_train, 'w')
    file_val = open(list_val, 'w')
    file_test = open(list_test, 'w')
    total_txt = os.listdir(label_original_path)
    num_txt = len(total_txt)
    list_all_txt = range(num_txt)
    num_train = int(num_txt * train_percent)
    num_val = int(num_txt * val_percent)
    num_test = num_txt - num_train - num_val
    train = random.sample(list_all_txt, num_train)
    # train 从 list_all_txt 取出 num_train 个元素
    # 所以 list_all_txt 列表只剩下了这些元素
    val_test = (i for i in list_all_txt if not i in train)
    # 再从 val_test 取出 num_val 个元素，val_test 剩下的元素就是 test
    val = random.sample(val_test, num_val)
    for i in list_all_txt:
        if i in train:
            shutil.copy(os.path.join(image_original_path, total_txt[i]), train_image_path)
            shutil.copy(os.path.join(label_original_path, total_txt[i]), train_label_path)
            file_train.write(os.path.join(train_image_path, total_txt[i]) + '\n')
        elif i in val:
            shutil.copy(os.path.join(image_original_path, total_txt[i]), val_image_path)
            shutil.copy(os.path.join(label_original_path, total_txt[i]), val_label_path)
            file_val.write(os.path.join(val_image_path, total_txt[i]) + '\n')
        else:
            shutil.copy(os.path.join(image_original_path, total_txt[i]), test_image_path)
            shutil.copy(os.path.join(label_original_path, total_txt[i]), test_label_path)
            file_test.write(os.path.join(test_image_path, total_txt[i]) + '\n')
    file_train.close()
    file_val.close()
    file_test.close()

if __name__ == '__main__':
    main()