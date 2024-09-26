import os
import math
from PIL import Image

TILED_WIDTH = 1920
TILED_HEIGHT = 1080

def add_tiled_postfix(image_pathname) -> str:
    
    # dirname 
    dir_name = os.path.dirname(image_pathname)

    # isolate basename of image
    image_filename = os.path.basename(image_pathname)

    # split filename to filename and extension
    filename, extension = os.path.splitext(image_filename)

    # generate tiled image filename
    tiled_filename = os.path.join(dir_name, filename + "_tiled_" + str(TILED_WIDTH) + "x" + str(TILED_HEIGHT) + extension)

    # return tiled image filename
    return tiled_filename


def image_tiler(base_image_path, tiled_width, tiled_height):

    # load base_image 
    base_image = Image.open(base_image_path)

    # get width, height 
    base_width, base_height = base_image.size

    # initialize tiled image 
    tiled_image = Image.new("RGB", (tiled_width, tiled_height), "black")
    
    # calculate amount of tiles needed to fill the tiled image
    x_tiles = math.ceil(tiled_width / base_width)
    y_tiles = math.ceil(tiled_height / base_height)

    # generate tiles
    for y in range(y_tiles):
        y_offset = base_height * y
        for x in range(x_tiles):
            x_offset = base_width * x
            tiled_image.paste(base_image, (x_offset, y_offset))

    return tiled_image 



# specify directory path 
DIRECTORY_PATH = './irix_wallpapers'

#List all files in the directory in the specified path
image_path_list = [os.path.join(DIRECTORY_PATH, file_name) for file_name in os.listdir(DIRECTORY_PATH)]

# Generate tiled pathname list 
image_tiled_path_list = [add_tiled_postfix(image_path) for image_path in image_path_list]

# Generate a list of items to process 
data_list = list(zip(image_path_list, image_tiled_path_list))


for each_image in data_list: 
    print("Base Image Path:  " + each_image[0])
    print("Tiled Image Path: " + each_image[1])
    print()
    print("Generating tiled image")
    tiled_image = image_tiler(each_image[0], TILED_WIDTH, TILED_HEIGHT)
    print()
    print("Saving tiled image to " + each_image[1])
    tiled_image.save(each_image[1], compress_level=1)
    print("-----------------------------------------------------------")

