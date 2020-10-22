import sys
from PIL import Image

original_image = 'DSCF2202.JPG'
try:
    picture = Image.open(original_image)
except Exception as e:
    print(*sys.exc_info(), sep='\n')
else:
    print(f'Original size of the picture is: {picture.size}')
    picture.save('compressed_' + original_image, optimied=True, quality=50)
