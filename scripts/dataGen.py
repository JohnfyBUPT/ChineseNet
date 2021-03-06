import sys
import getopt
from PIL import Image, ImageFilter, ImageChops
import numpy as np
import scipy.misc
import os
import re
import PIL.ImageOps
import cv2

def main(argv):
    in_dir = '../data/test_temp/'
    out_dir = '../data/check_gen/'
    img_names = os.listdir(in_dir)
    is_jpg = re.compile(r'.+?\.jpg')
# do interpolation to generate (32,32) images
   # for name in img_names:
   #     if(is_jpg.match(name)):
   #         img = cv2.imread(in_dir + name)
   #         res = cv2.resize(img, (32, 32), interpolation = cv2.INTER_CUBIC)
   #         cv2.imwrite(out_dir + name, res)
# resize the image
    # for name in img_names:
    #     if(is_jpg.match(name)):
    #         image = Image.open(in_dir + name)
    #         image = image.resize((48, 48), Image.ANTIALIAS)
    #         image.save(out_dir + name)
# invert the image
    # for name in img_names:
    #     if(is_jpg.match(name)):
    #         image = Image.open(in_dir + name)
    #         inverted_image = PIL.ImageOps.invert(image)
    #         inverted_image.save(in_dir + name)
# convert to grayscale
   # for name in img_names:
   #     if(is_jpg.match(name)):
   #         image = Image.open(in_dir + name).convert('L')
   #         image.save(in_dir + name)

# shifting pixels
   # for name in img_names:
   #     if(is_jpg.match(name)):
   #         img_orig = Image.open(in_dir + name)
   #         for i in range(-3, 4):
   #             for j in range(-3, 4):
   #                 img_gen = ImageChops.offset(img_orig, 3*i, 3*j)
   #                 img_gen.save(out_dir + name.strip('.jpg') + '_%d%d.jpg' %(i, j))
   # print('pixel shifting completed.')

# gaussian
#    print('performing gaussian blur on the original images...')
#    for name in img_names:
#        if(is_jpg.match(name)):
#            image = Image.open(out_dir + name)
#            image = image.filter(ImageFilter.GaussianBlur(radius=1)) 
#            image.save(out_dir + name.strip('g.jpg') + 'g.jpg')
#    print('gaussian blur completed.')
# rotation
   # print('performing rotation on the original images...')
   # for name in img_names:
   #     if(is_jpg.match(name)):
   #         image = Image.open(in_dir + name)
   #         for i in (-15, -10, 10, 15):
   #             image_r = image.rotate(i)
   #             image_r.save(out_dir + name[:len(name) - 4] + 'r' + str(i) + '.jpg')
   # print('rotation completed.')
#threshold
    for name in img_names:
        if(is_jpg.match(name)):
            data = np.array(Image.open(in_dir+name))
            index = data >=  128
            data[index] = 255
            index = data < 128
            data[index] = 0
            image = Image.fromarray(data)
            image.save(in_dir + name)

if __name__ == "__main__":
    main(sys.argv[1:])
