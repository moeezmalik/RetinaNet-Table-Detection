import cv2 as opencv
import os

# Configurations
image_path = "dataset/table-dataset/images/PMC2816861_00002.jpg"
x1 = 49
y1 = 565
x2 = 559
y2 = 705

# Open the image
image = opencv.imread(image_path)

# Draw the bounding box
opencv.rectangle(image, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

# Show the image
opencv.imshow("test-image", image)
opencv.waitKey(0)
