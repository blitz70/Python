# image : channels, split, merge

from PIL import Image

img1 = Image.open('pic_rgb.jpg')
img1.show()

# split
r1, g1, b1 = img1.split()
r1.show()
g1.show()
b1.show()

# merge
img2 = Image.open('pic_death.jpg')
img3 = Image.open('pic_land.jpg')
r2, g2, b2 = img2.split()
r3, g3, b3 = img3.split()
img4 = Image.merge('RGB', (r2, g3, b3))
img2.show()
img3.show()
img4.show()

