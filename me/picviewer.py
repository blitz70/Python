# directory picture viewer

from PIL import Image

path = r'D:/Files/꼬마아이숲_풀잎반_김규리/'

pics = []  # picture list
for x in range(1, 70):
    pics.append(str(x)+'.jpg')

bg = Image.new('RGB', (5000, 5000))  #background

_y = -1
for x in range(len(pics)):
    img0 = Image.open(path + pics[x])
    img = img0.resize((int(img0.size[0]/8), int(img0.size[1]/8)))  # 1/8
    if x % 10 is 0:
        _y += 1
    bg.paste(img, (500 * (x % 10), 500 * _y))

bg.save('curie.jpg')
bg.show()
