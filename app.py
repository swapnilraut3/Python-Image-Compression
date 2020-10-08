import os
from PIL import Image

print(os.getcwd())
print(os.chdir('Desktop'))
print(os.getcwd())
print(os.listdir())

#
original_image = 'IMG_20200224_135728.jpg'
picture = Image.open(original_image)

print(f'Original size of the picture is: {picture.size}')
picture.save('compressed_' + original_image, optimied=True, quality=50)
