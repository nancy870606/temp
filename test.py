import cv2
import numpy as np
from matplotlib import  pyplot as plt
img=cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('cat1.jpg',img)
print(img)
cv2.imshow('cat',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()