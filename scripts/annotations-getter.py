from pydoc import classname
import pandas as pd
import xml.etree.cElementTree as et

# Path to the assigned IDs CSV file
pathToImageNamesCSV = "dataset/table-dataset/id-assignments.csv"
pathToAnnotationsXML = "dataset/table-dataset/test.xml"

# Read the CSV file and load the image name and the assigned IDs
# imageNames = pd.read_csv(pathToImageNamesCSV)

# This is the root of the XML tree
tree = et.parse(pathToAnnotationsXML)
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

print(filename)
print(className)
print(x1)
print(y1)
print(x2)
print(y2)