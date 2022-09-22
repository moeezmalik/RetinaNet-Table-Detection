# This script will copy the the files (images in the context of table detection)
# from the source folder and copy them over to the target folder based
# on the CSV file provided

import pandas as pd
from shutil import SameFileError, copyfile
from os.path import join

csv_path = "dataset/table-dataset/csv/test.csv"
source_folder = "dataset/table-dataset/images/"
target_folder = "dataset/table-dataset/visualise-test-resnet101/"


def main():
    
    # Read the dataframe and convert to python list
    csv_df = pd.read_csv(csv_path, names=['id', 'x1', 'y1', 'x2', 'y2', 'class'])
    csv_list = csv_df.values.tolist()
    


    # Attempt to copy the files and catch errors if any
    count = 0
    for row in csv_list:

        file = row[0]                                   # Get the file name
        source_file = join(source_folder, file)         # Join to get the full paths
        target_file = join(target_folder, file)         # Join to get the full paths

        try:
            copyfile(source_file, target_file)
            count += 1

        except SameFileError:
            print("Skipping Duplicate: " + str(file))

    print("Copied " + str(count) + " file/s")

if __name__ == "__main__":
    main()