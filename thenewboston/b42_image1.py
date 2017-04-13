# image : show, crop, paste

from PIL import Image

#show
img1 = Image.open('pic_big.jpg')
print(img1.size, img1.format, img1.mode)
img1.show()

#crop
area1 = (0, 0, img1.size[0]*2/3, img1.size[1])
img2 = img1.crop(area1)
img2.show()

#paste
img3 = Image.open('pic_small.jpg')
area2 = (200, 100, 200+img3.size[0], 100+img3.size[1])
img1.paste(img3, area2)
img1.show()