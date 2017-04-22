# image : convert, ImageFilter

from PIL import Image, ImageFilter

img = Image.open('pic_big.jpg')
img.show()

# convert
bw = img.convert('L')
bw.show()

# ImageFilter
blur = img.filter(ImageFilter.BLUR)
sharp = img.filter(ImageFilter.SHARPEN)
edge = img.filter(ImageFilter.FIND_EDGES)
blur.show()
sharp.show()
edge.show()