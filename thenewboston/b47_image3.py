# image : resize, transpose

from PIL import Image

img = Image.open('pic_big.jpg')
img.show()

# resize
square = img.resize((300, 300))
square.show()

# transpose
flip = img.transpose(Image.FLIP_TOP_BOTTOM)
spin = img.transpose(Image.ROTATE_180)
flip.show()
spin.show()