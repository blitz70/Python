# image : channels

from PIL import Image

img1 = Image.open('pic_rgb.jpg')
img1.show()
print(img1.size, img1.format, img1.mode)

r, g, b = img1.split()
r.show()
g.show()
b.show()

