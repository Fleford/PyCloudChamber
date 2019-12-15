import numpy as np
import cv2

img = cv2.imread("profilepic.jpg", cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (100, 150), (255, 255, 255), 10)    # BGR
cv2.rectangle(img, (15, 25), (200, 150), (255, 255, 0), 5)
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]])
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV text!", (100, 330), font, 3, (200, 255, 0), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
