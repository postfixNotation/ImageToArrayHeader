#!/usr/bin/env python3
# image file name and greyscale threshold
# are passed as terminal parameters
# for instance: ./image_to_header.py image.png 128

from PIL import Image
import sys

def grayscale_to_binary(grayscale):
    if grayscale > int(sys.argv[2]): # threshold
        return 1
    else:
        return 0

im = Image.open(sys.argv[1],"r")
im = im.convert("L")
file = open("image.h", "w")

width = im.size[0]
height = im.size[1]

result_list = "#ifndef IMAGE_H_\n#define IMAGE_H_\n\n"
result_list += "#include <stdint.h>\n\n"
result_list += "uint8_t image[] = {"

for y in range(height):
    byte_value = 0
    for x in range(width):
        grayscale = im.getpixel((x,y))
        value = grayscale_to_binary(grayscale)
        byte_value = byte_value | (value << (x % 8))
        if x % 8 == 7:
            result_list += (str(byte_value)+",")
            byte_value = 0

result_list += "};\n\n"
result_list += "#endif // IMAGE_H_\n\n"

file.write(result_list)
#im.save("grayscale.png")

