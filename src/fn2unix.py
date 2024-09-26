import os

# specify directory path 
DIRECTORY_PATH = './irix_wallpapers'

# List all files in the directory in the specified path
file_list = os.listdir(DIRECTORY_PATH)

for each in file_list: 
    # join directory path with filename 
    full_old = os.path.join(DIRECTORY_PATH, each)

    # compose new unix compliant filename
    new_filename = full_old.replace(" ", "_").lower()

    # rename file 
    os.rename(full_old, new_filename)

    # print feedback 
    print(full_old + " " + new_filename)


