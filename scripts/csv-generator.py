import pandas as pd

pathToImageNames = "dataset/table-dataset/csv/id-assignments.csv"
pathToAnnotationsCSV = "dataset/table-dataset/csv/all-annotations-no-original.csv"

pathToSaveTrain = "dataset/table-dataset/csv/train.csv"
pathToSaveValidation = "dataset/table-dataset/csv/val.csv"
pathToSaveTest = "dataset/table-dataset/csv/test.csv"

noOfTestImages = 51
noOfValidationImages = 280

def mergeWithAnnotationsAndSaveCSV(images, annotations, pathToSaveCSV):

    images = images.drop(columns=['original-name'])
    merged = pd.merge(left=images, right=annotations, how='left', on="id")
    merged.to_csv(path_or_buf=pathToSaveCSV, header=False, index=False)

def csvToDataFrame(pathToCSV):
    return pd.read_csv(pathToCSV)

def main():
    print("Starting CSV Generator")

    # Get all the image annotations
    imageAnnotations = csvToDataFrame(pathToAnnotationsCSV)

    # Get the test images
    allImageNames = csvToDataFrame(pathToImageNames)
    testImages = allImageNames.sample(n=noOfTestImages)
    

    # Get the validation images
    imageNamesWithoutTest = allImageNames.drop(testImages.index)
    validationImages = imageNamesWithoutTest.sample(n=noOfValidationImages)

    # Get the train images
    trainImages = imageNamesWithoutTest.drop(validationImages.index)

    # Save Test Images to CSV File
    mergeWithAnnotationsAndSaveCSV(testImages, imageAnnotations, pathToSaveTest)
    print("No. of Test Images Saved: " + str(testImages.shape[0]))

    # Save Validation Images to CSV File
    mergeWithAnnotationsAndSaveCSV(validationImages, imageAnnotations, pathToSaveValidation)
    print("No. of Test Images Saved: " + str(validationImages.shape[0]))

    # Save Train Images to CSV File
    mergeWithAnnotationsAndSaveCSV(trainImages, imageAnnotations, pathToSaveTrain)
    print("No. of Test Images Saved: " + str(trainImages.shape[0]))



if __name__ == "__main__":
    main()