import cv2 as opencv

image_path = "dataset/visualise-test/test-image.jpg"

x1 = 180
y1 = 825
x2 = 1468
y2 = 1382

image = opencv.imread(image_path)

opencv.rectangle(image, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

opencv.imshow("Preview", image)
opencv.waitKey(0)
opencv.destroyAllWindows()