import cv2
import os
def draw_bounding_boxes(image_path, label_path, output_image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Read the label file
    with open(label_path, 'r') as f:
        labels = f.readlines()

    # Draw bounding boxes for each object
    for label in labels:
        # Parse the label information
        class_id, x_center, y_center, width, height = label.strip().split(' ')
        class_id = int(class_id)
        x_center = float(x_center)
        y_center = float(y_center)
        width = float(width)
        height = float(height)

        # Convert normalized coordinates to image coordinates
        x_min = int((x_center - width / 2) * image.shape[1])
        y_min = int((y_center - height / 2) * image.shape[0])
        x_max = int((x_center + width / 2) * image.shape[1])
        y_max = int((y_center + height / 2) * image.shape[0])

        # Draw the bounding box
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        # Optionally, display class label and confidence score (if available)
        # ...

    # Save the result image
    cv2.imwrite(output_image_path, image)
if __name__ == "__main__":
    image_dir = r'C:\Users\user\Desktop\PRBNet_Pytorch_DevOps-main\yolov7_prb\datasets\DUO20\test\images'  # Directory containing original images
    label_dir = r'C:\Users\user\Desktop\PRBNet_Pytorch_DevOps-main\yolov7_prb\datasets\DUO20\test\labels'  # Directory containing YOLO label files
    output_dir = r'C:\Users\user\Desktop\PRBNet_Pytorch_DevOps-main\yolov7_prb\ZOurWork\datasets\Duo20test'  # Directory to save result images

    for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)
        label_path = os.path.join(label_dir, image_name.split('.')[0] + '.txt')
        output_image_path = os.path.join(output_dir, image_name)

        draw_bounding_boxes(image_path, label_path, output_image_path)