from cmath import nan
import cv2 as opencv
import pandas as pd
from os.path import join

annotationsPath = "dataset/table-dataset/csv/all-annotations-no-original.csv"
imageFolder = "dataset/table-dataset/images/"

idAssignmentsFile = "dataset/table-dataset/csv/id-assignments.csv"
doubtFullImagesCSV = "dataset/table-dataset/csv/doubtful.csv"

def csvToDataFrame(pathToCSV):
    return pd.read_csv(pathToCSV)

def visualiseAnnotations(imageName, imageFolder, annotationsPath):
    print("Starting Visualiser")

    # Loading up the image as OpenCV object
    pathToImage = join(imageFolder, imageName)
    currentImage = opencv.imread(pathToImage)

    # Load annotations for the current image
    annotations = csvToDataFrame(annotationsPath)
    match = annotations.loc[annotations['id'] == imageName].values.tolist()

    # Draw rectangles for all annotations
    for box in match:

        print(box)

        if(box[1] or box[2] or box[3] or box[4] is nan):
            print("No Annotations")
        else:

            x1 = int(box[1])
            y1 = int(box[2])
            x2 = int(box[3])
            y2 = int(box[4])
            
            opencv.rectangle(currentImage, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

    

    opencv.imshow(imageName, currentImage)
    opencv.waitKey(0)
    opencv.destroyAllWindows()




def main():
    visualiseAnnotations("image_809.jpg", imageFolder, annotationsPath)

    # idAssignments = csvToDataFrame(idAssignmentsFile)
    # doubtfulImages = csvToDataFrame(doubtFullImagesCSV).values.tolist()

    # print("Total Doubtful Images: " + str(len(doubtfulImages)))

    # count = 0

    # for image in doubtfulImages:

    #     match = idAssignments.loc[idAssignments['original-name'] == str(image[0])].values.tolist()
    #     if(len(match) > 0):

    #         assignedImageID = match[0][0]
    #         visualiseAnnotations(assignedImageID, imageFolder, annotationsPath)

    #         count += 1

    # print("Total Matches Found in Assignments: " + str(count))

if __name__ == "__main__":
    main()