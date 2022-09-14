from os import listdir
from os.path import isfile, join
import pandas as pd
import xml.etree.cElementTree as et

# Path to the assigned IDs CSV file
pathToImageNamesCSV = "dataset/table-dataset/id-assignments.csv"
pathToXMLAnnotationsFolder = "dataset/table-dataset/annotations/"

# Read the CSV file and load the image name and the assigned IDs
# imageNames = pd.read_csv(pathToImageNamesCSV)

def xmlAnnotationsToList(pathToXML):

    # This is the root of the XML tree
    tree = et.parse(pathToXML)
    root = tree.getroot()

    # Here we extract the file name
    filename = root.find("filename").text

    # Now we proceed and extract the class name and the bounding box
    objectRoot = root.find("object")

    # This is the class name
    className = objectRoot.find("name").text


    # Now we go further into the tree and get the bounding box
    bndBoxRoot = objectRoot.find("bndbox")

    x1 = bndBoxRoot.find("xmin").text
    y1 = bndBoxRoot.find("ymin").text
    x2 = bndBoxRoot.find("xmax").text
    y2 = bndBoxRoot.find("ymax").text

    return [filename, x1, y1, x2, y2, className]

def annotationsXMLToDataFrame(pathToAnnotationsFolder):

    totalElementsFound = 0
    totalFilesFound = 0
    totalAnnotationsRead = 0

    listOfAnnotations = []

    for f in listdir(pathToAnnotationsFolder):

        totalElementsFound += 1

        completePathToFile = join(pathToAnnotationsFolder, f)

        if isfile(completePathToFile):
            totalFilesFound += 1
            readAnnotations = xmlAnnotationsToList(completePathToFile)

            if(len(readAnnotations) == 6):
                totalAnnotationsRead += 1
                listOfAnnotations.append(readAnnotations)

    print("Total Elements Found: " + str(totalElementsFound))
    print("Total Files Found: " + str(totalFilesFound))
    print("Total Annotations Read: " + str(totalAnnotationsRead))

    imageLabels = pd.DataFrame(listOfAnnotations, columns=["original-name", "x1", "y1", "x2", "y2", "class"])
    # print(imageLabels)
    return imageLabels

def imageNamesCSVToDataFrame(pathToCSV):
    return pd.read_csv(pathToCSV)

def main():

    imageLabels = annotationsXMLToDataFrame(pathToXMLAnnotationsFolder)
    imageNames = imageNamesCSVToDataFrame(pathToImageNamesCSV)

    print("")
    print(imageNames.dtypes)
    print("")
    print(imageLabels.dtypes)

    joined = pd.merge(left=imageNames, right=imageLabels, how='left', on="original-name")
    print(joined)

if __name__ == "__main__":
    main()