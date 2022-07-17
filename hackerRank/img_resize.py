from PIL import Image
from matplotlib import pyplot as plt
import cv2 ,glob


def resize_img(path):
    im = Image.open(path)
    left = 200
    top = 200
    right = 1310
    bottom = 1300
    im1 = im.crop((left, top, right, bottom))
    # im1.show()
    print(path)
    im1.save(path)

imdir = ''
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

for img in files:
    resize_img(img)
# resize_img(r"Screenshot (180).png")

