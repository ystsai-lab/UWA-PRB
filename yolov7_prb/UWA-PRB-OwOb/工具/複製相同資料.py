import os
import shutil

def get_file_list(dataset_dir):
    file_list = []
    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_common_files(file_list1, file_list2):
    """
    取得兩個檔案列表中相同的檔案

    Args:
        file_list1: 第一個檔案列表
        file_list2: 第二個檔案列表

    Returns:
        包含相同檔案的 list
    """
    return list(set(file_list1) & set(file_list2))

def get_relative_paths(selected_files, base_dir):
    relative_paths = [os.path.relpath(file, base_dir) for file in selected_files]
    return relative_paths

def copy_files_to_destination(file_list, source_dir, destination_dir):
    for file in file_list:
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(destination_dir, file)
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy(source_path, destination_path)

if __name__ == "__main__":
    # 設定資料集路徑
    dataset_dir_source = "../../datasets/DUOmain"
    dataset_dir_copy= "../../datasets/DUOreset20"
    new_dataset_dir = "../../datasets/DUO20"

    # 獲取檔案列表
    file_list_source = get_file_list(dataset_dir_source)
    file_list_copy = get_file_list(dataset_dir_copy)

    # 取得兩個資料集中相同的檔案
    common_files = get_common_files(
        [os.path.relpath(file, dataset_dir_source) for file in file_list_source],
        [os.path.relpath(file, dataset_dir_copy) for file in file_list_copy]
    )

    # 取得選擇的檔案
    selected_files_source = common_files
    selected_labels_source= [image.replace("images", "labels").replace(".jpg", ".txt") for image in selected_files_source]

    # 提取相對路徑
    relative_paths_images_fs = get_relative_paths(
        [os.path.join(dataset_dir_source, file) for file in selected_files_source], dataset_dir_source
    )
    relative_paths_labels_fs = get_relative_paths(
        [os.path.join(dataset_dir_source, file) for file in selected_labels_source], dataset_dir_source
    )

    print(len(selected_files_source))
    print(len(selected_labels_source))

    # 將檔案複製到新的目的地目錄
    copy_files_to_destination(relative_paths_images_fs, dataset_dir_source, new_dataset_dir)
    copy_files_to_destination(relative_paths_labels_fs, dataset_dir_source, new_dataset_dir)
