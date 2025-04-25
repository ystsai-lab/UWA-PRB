import os
import random
import shutil
from collections import defaultdict

def get_file_list(dataset_dir):
    """
    獲取指定目錄下所有 image 檔案名稱

    Args:
        dataset_dir: 資料集目錄

    Returns:
        包含所有 image 檔案名稱的 list
    """
    file_list = []
    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            if file.endswith(".jpg"):
                file_list.append(os.path.join(root, file))
    return file_list


def output_dataset(file_list, output_dir, subdir_name):
    subdir_path = os.path.join(output_dir, subdir_name)
    subdir_images = os.path.join(subdir_path, "images")
    os.makedirs(subdir_images, exist_ok=True)
    subdir_labels = os.path.join(subdir_path, "labels")
    os.makedirs(subdir_labels, exist_ok=True)

    for file in file_list:
        img_path = file
        file_name = os.path.basename(file)
        file_name_without_ext = os.path.splitext(file_name)[0]
        label_path = os.path.join(os.path.dirname(file).replace("images", "labels"), file_name_without_ext + ".txt")
        shutil.copy2(img_path, os.path.join(subdir_images, file_name))
        shutil.copy2(label_path, os.path.join(subdir_labels, os.path.basename(label_path)))
def split_dataset(file_list, train_ratio, valid_ratio, test_ratio, input_dir, output_dir):
    """
    將 dataset 重新分成 train、valid 和 test 三部分

    Args:
        file_list: dataset 中的所有檔案名稱 list
        train_ratio: train 集的比例
        valid_ratio: valid 集的比例
        test_ratio: test 集的比例
        input_dir: 原始資料集目錄
        output_dir: 輸出目錄

    Returns:
        包含 train、valid 和 test 集檔案名稱的 list
    """
    num_files = len(file_list)
    num_train = int(num_files * train_ratio)
    num_valid = int(num_files * valid_ratio)
    num_test = int(num_files * test_ratio)
    print(num_files,num_train,num_valid,num_test)

    # 打亂檔案索引
    random.shuffle(file_list)

    # 將檔案分配到各個集合中
    train_files = file_list[:num_train]
    valid_files = file_list[num_train:num_train + num_valid]
    test_files = file_list[num_train + num_valid:]

    # 輸出分配出來的結果數量
    print("Train: {}".format(len(train_files)))
    print("Valid: {}".format(len(valid_files)))
    print("Test: {}".format(len(test_files)))

    # # 輸出 train 集
    # train_output_dir = os.path.join(output_dir, "train")
    # train_output_dir_images = os.path.join(train_output_dir, "images")
    # os.makedirs(train_output_dir_images, exist_ok=True)
    # train_output_dir_labels = os.path.join(train_output_dir, "labels")
    # os.makedirs(train_output_dir_labels, exist_ok=True)
    #
    # for file in test_files:
    #     img_path = file
    #     file_name = os.path.basename(file)
    #     file_name_without_ext = os.path.splitext(file_name)[0]  # 取得不包含副檔名的部分
    #     label_path = os.path.join(os.path.dirname(file).replace("images", "labels"), file_name_without_ext + ".txt")
    #     shutil.copy2(img_path, os.path.join(train_output_dir_images, file_name))
    #     shutil.copy2(label_path, os.path.join(train_output_dir_labels, os.path.basename(label_path)))
    output_dataset(train_files, output_dir, "train")
    output_dataset(valid_files, output_dir, "valid")
    output_dataset(test_files, output_dir, "test")

    return train_files, valid_files, test_files


if __name__ == "__main__":
    # 設定 dataset 目錄
    input_dir = "../../datasets/DUOmain640"
    # 設定輸出目錄
    output_dir = "../../datasets/DUOreset20"
    # 取得 dataset 中的所有檔案名稱
    file_list = get_file_list(input_dir)
    # 將 dataset 重新分成 train、valid 和 test 三部分
    split_dataset(file_list, 0.8, 0.1, 0.1, input_dir, output_dir)
