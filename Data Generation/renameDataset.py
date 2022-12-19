import os

# Set the directory that contains the sub-folders with the files to be renamed
root_dir = 'J:\CMPT 732 Project\CMPT732_data_yolov5\labels'

# Set the old and new file names
old_name = 'bounding_box_2d_loose'
new_name = 'rgb'

# Loop through the sub-directories in the root directory
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # Check if the file name begins with the old name
        if file.startswith(old_name):
            # Construct the full path of the file
            file_path = os.path.join(subdir, file)
            # Construct the new file name
            new_file_name = file.replace(old_name, new_name)
            # Construct the full path of the new file name
            new_file_path = os.path.join(subdir, new_file_name)
            # Rename the file
            os.rename(file_path, new_file_path)
