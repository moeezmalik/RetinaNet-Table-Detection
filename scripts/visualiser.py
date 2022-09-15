import cv2 as opencv
import pandas as pd
from os.path import join

annotationsPath = "dataset/table-dataset/csv/all-annotations.csv"
imageFolder = "dataset/table-dataset/images/"

def csvToDataFrame(pathToCSV):
    return pd.read_csv(pathToCSV)

def visualiseAnnotations(imageName, imageFolder, annotationsPath):
    print("Starting Visualiser")

    annotations = csvToDataFrame(annotationsPath)

    match = annotations.loc[annotations['id'] == imageName].values.tolist()

    for box in match:
        print(box[2])

    pathToImage = join(imageFolder, imageName)




def main():
    visualiseAnnotations("image_1.jpg", imageFolder, annotationsPath)

if __name__ == "__main__":
    main()