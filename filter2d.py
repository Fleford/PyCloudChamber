import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('opencv_logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img", img)
kernel = np.ones((5,5), np.float32)/25
kernel = np.array([[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]])

kernel2 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

kernel = kernel / np.sum(kernel)
print(kernel)

dst = cv2.filter2D(img,-1,kernel)

dst = cv2.subtract(dst, img)
# dst = cv2.filter2D(dst,-1,kernel)

cv2.imshow("filter2D", dst)
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()