import cv2
import os


def draw_boxes(image_path, label_path, output_path, class_names):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Cannot read image {image_path}")
        return

    height, width, _ = image.shape

    # 读取标签文件
    if not os.path.exists(label_path):
        print(f"Error: Label file {label_path} does not exist")
        return

    with open(label_path, 'r') as file:
        labels = file.readlines()

    # 定义每个类别的颜色
    colors = {
        0: (0, 0, 255)  # 红色
        , 1: (230, 114, 30) #深橘
       , 2:(255, 0, 0)  # 深蓝色
        ,3: (128, 0, 128) #紫色
        ,4:(225, 162, 173) # 粉色
    }

    for label in labels:
        parts = label.strip().split()
        class_id = int(parts[0])
        x1 = float(parts[1])
        y1 = float(parts[2])
        x2 = float(parts[5])
        y2 = float(parts[6])

        # 计算实际像素坐标
        x1 = int(x1 * width)
        y1 = int(y1 * height)
        x2 = int(x2 * width)
        y2 = int(y2 * height)

        # 选择框的颜色
        color = colors.get(class_id, (255, 255, 255))  # 默认颜色为白色
        # 在图像上绘制矩形框
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        # 在图像上绘制类别名称
        cv2.putText(image, class_names[class_id], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # 保存输出图像
    cv2.imwrite(output_path, image)


# 示例使用
image_path = r'C:\Users\user\Desktop\testdataset\DUO20\test\new\train_4881.jpg'
label_path = r'C:\Users\user\Desktop\testdataset\DUO20\test\new_label\train_4881.txt'
output_path = r'C:\Users\user\Desktop\PRBNet_Pytorch_DevOps-main\yolov7_prb\ZOurWork\datasets\Duo20label\ta4881.jpg'
class_names = ['echinus', 'holothurian', 'scallop', 'starfish']  # 类别名称列表

draw_boxes(image_path, label_path, output_path, class_names)
