import os
import json

def rename_files_and_update_annotations(dataset_path, new_prefix):
    # 產生新的_annotations.coco.json檔案的完整路徑
    old_annotations_path = os.path.join(dataset_path, "_annotations.coco.json")
    new_annotations_path = os.path.join(dataset_path, f"{new_prefix}_annotations.coco.json")

    # 讀取舊的_annotations.coco.json檔案
    with open(old_annotations_path, 'r') as f:
        annotations_data = json.load(f)

    # 取得所有檔案清單
    files = os.listdir(dataset_path)

    # 過濾出所有的圖片檔案（假設圖片都是以.jpg結尾的）
    image_files = [file for file in files if file.endswith('.jpg')]

    # 依序處理每一張圖片
    for i, image_file in enumerate(image_files, start=1):
        # 產生新的檔案名稱
        new_filename = f"{new_prefix}{i:04d}.jpg"

        # 產生原始圖片檔案的完整路徑
        old_image_path = os.path.join(dataset_path, image_file)

        # 產生新的圖片檔案的完整路徑
        new_image_path = os.path.join(dataset_path, new_filename)

        # 進行檔案改名
        os.rename(old_image_path, new_image_path)

        # 更新_annotations.coco.json中的檔案名稱
        for annotation in annotations_data['images']:
            if annotation['file_name'] == image_file:
                annotation['file_name'] = new_filename

    # 寫入更新後的_annotations.coco.json檔案
    with open(new_annotations_path, 'w') as f:
        json.dump(annotations_data, f, indent=2)

if __name__ == "__main__":
    dataset_path = "C:\\Users\\user\\Downloads\\DUOcoco\\valid"  # 修改為你的資料集路徑
    new_prefix = "valid"  # 修改為你希望的新檔案名稱前綴

    rename_files_and_update_annotations(dataset_path, new_prefix)
