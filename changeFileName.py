import os
import re

def callback(match):
    x = int(match.group(1))
    if x < 50:
      return '_{}_'.format(x + 25)
    else:
      return '_{}_'.format(x)
    return '_{}_'.format(x + 75)

def replace_substring_in_filenames(folder, old_range, new_range):

  # Get a list of all the filenames in the given folder
    filenames = os.listdir(folder)
    print((len(filenames)-1)/4)

  # Loop through the filenames and replace the old substring with the new one
    for filename in reversed(filenames):
    
        # pattern = re.compile(r'_[0-9]_')
        pattern = re.compile(r'_(\d+)_')
        # Use the re.sub() function to replace the 'X' part of the pattern with the new range
        new_filename = pattern.sub(callback, filename)
        # Use the os.rename() function to rename the file
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))

# Use the function
replace_substring_in_filenames(os.getcwd(), '0', '20')
