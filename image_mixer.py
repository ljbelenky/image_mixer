from PIL import Image
import numpy as np 

fire = np.array(Image.open('fire.jpg'))
land = np.array(Image.open('land.jpg'))

threshold = 3*255/2

mask = land.sum(axis=2)>threshold

mask = np.stack([mask, mask, mask], axis = 2)

combined_image = (fire*(1-mask) + land*(mask)).astype(np.uint8)

i = Image.fromarray(combined_image)
i.show()