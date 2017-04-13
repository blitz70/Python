# image : merge

from PIL import Image

img1 = Image.open('pic_death.jpg')
img2 = Image.open('pic_land.jpg')
r1, g1, b1 = img1.split()
r2, g2, b2 = img2.split()
img3 = Image.merge('RGB', (r1, g2, b2))
img1.show()
img2.show()
img3.show()