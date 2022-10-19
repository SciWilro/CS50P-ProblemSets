__author__ = 'Wilro - https://github.com/SciWilro'
'''_summary_
Overlay `shirt.png` file onto user specified image, and exports new image
Args:
    sys.argv[1] (str): name (or path) of a JPEG or PNG to read
    sys.argv[2] (str): name (or path) of a JPEG or PNG to write
'''

import sys
import os
from PIL import Image
from PIL import ImageOps

ext_list = ['.jpg','.jpeg','.png']

def check_args():
    if len(sys.argv) != 3:
        sys.exit("Program expects 2 cmdline arguments")
    if os.path.splitext(sys.argv[1].lower())[1] not in ext_list or os.path.splitext(sys.argv[2].lower())[1] not in ext_list:
        sys.exit("Accepted extensions are .jpg, .jpeg, or .png - Case insensitive")
    
    if os.path.splitext(sys.argv[1].lower())[1] != os.path.splitext(sys.argv[2].lower())[1]:
        sys.exit("Arguments must have same extension")
        
    if os.path.exists(sys.argv[1]) is False:
        sys.exit(f"Specified file {sys.argv[1]} does not exist")

def main():
    check_args()
    
    # Open
    img1 = Image.open(fp=sys.argv[1])
    img_shirt = Image.open(fp="shirt.png")
    # Resize and crop
    size = img_shirt.size
    output = ImageOps.fit(img1, size)
    # Overlay shirt.png
    output.paste(img_shirt, img_shirt) # second argument is mask (I think)
    # Save
    output.save(sys.argv[2])
    

if __name__ == '__main__':
    main()
