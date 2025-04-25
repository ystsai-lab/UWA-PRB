import os
import random
import shutil
from collections import defaultdict

def get_file_list(dataset_dir):
    """
    取得 dataset 中的所有檔案名稱

    Args:
        dataset_dir: dataset 所在的目錄

    Returns:
        包含所有檔案名稱的 list
    """
    file_list = []
    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_random_indices(file_list, ratio):
    """
    取得 dataset 中 1/ratio 的隨機索引

    Args:
        file_list: dataset 中的所有檔案名稱 list
        ratio: 要取出的比例

    Returns:
        包含隨機索引的 list
    """
    num_files = len(file_list)
    num_selected = int(num_files * ratio)
    random_indices = random.sample(range(num_files), num_selected)
    return random_indices

def get_selected_files(file_list, random_indices):
    """
    取得 dataset 中 1/ratio 的對應檔案

    Args:
        file_list: dataset 中的所有檔案名稱 list
        random_indices: 包含隨機索引的 list

    Returns:
        包含對應檔案名稱的 list
    """
    selected_images = [file_list[index] for index in random_indices if "images" in file_list[index]]
    selected_labels = [image.replace("images", "labels").replace(".jpg", ".txt") for image in selected_images]
    return selected_images, selected_labels


def extract_labels_from_images(selected_images):
    """
    從 images 的檔案中提取對應的 labels 檔案

    Args:
        selected_images: 包含 images 檔案名稱的 list

    Returns:
        包含對應 labels 檔案名稱的 list
    """
    selected_labels = [image.replace("images", "labels").replace(".jpg", ".txt") for image in selected_images]
    return selected_labels



def get_relative_paths(selected_files, base_dir):
    """
    取得相對路徑列表

    Args:
        selected_files: 包含完整路徑的檔案名稱 list
        base_dir: 基本目錄，將用於計算相對路徑

    Returns:
        包含相對路徑的 list
    """
    relative_paths = [os.path.relpath(file, base_dir) for file in selected_files]
    return relative_paths

def copy_files_to_destination(file_list, source_dir, destination_dir):
    """
    將檔案複製到目的地目錄

    Args:
        file_list: 包含完整路徑的檔案名稱 list
        source_dir: 原始目錄
        destination_dir: 目的地目錄
    """
    for file in file_list:
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(destination_dir, file)
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)  # 確保目的地目錄存在
        shutil.copy(source_path, destination_path)


if __name__ == "__main__":
    dataset_dir = "../../datasets/DUOreset20"
    ratio = 1/5
    new_dataset_dir = "../../datasets/split_dataset_2"  # 新的目的地目錄
    for root, dirs, files in os.walk(dataset_dir):
        print(f"root: {root}, dirs: {dirs}, files: {files}")

    file_list = get_file_list(dataset_dir)
    random_indices = get_random_indices(file_list, ratio)
    selected_images, selected_labels = get_selected_files(file_list, random_indices)

    # 提取相對路徑
    relative_paths_images = get_relative_paths(selected_images, dataset_dir)
    relative_paths_labels = get_relative_paths(selected_labels, dataset_dir)

    print(len(selected_images))
    print(len(selected_labels))

    # 將檔案複製到新的目的地目錄
    copy_files_to_destination(relative_paths_images, dataset_dir, new_dataset_dir)
    copy_files_to_destination(relative_paths_labels, dataset_dir, new_dataset_dir)
