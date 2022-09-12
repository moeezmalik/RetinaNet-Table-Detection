import cv2 as opencv
import os

# Configurations
image_path = "dataset/visualise-test/test-image.jpg"
x1 = 187
y1 = 830
x2 = 1470
y2 = 1382

# Open the image
image = opencv.imread(image_path)

# Draw the bounding box
opencv.rectangle(image, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

# Show the image
opencv.imshow("test-image", image)
opencv.waitKey(0)
