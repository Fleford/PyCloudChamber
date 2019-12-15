import cv2
import numpy as np

kernel = np.ones((2, 2), np.uint8)

cap = cv2.VideoCapture(2)
ret, frame = cap.read()

gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_frame_avg = gray_frame
diff_old = gray_frame

while True:
    ret, frame = cap.read()

    # Extract traces
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.subtract(gray_frame, gray_frame_avg)
    ret, diff = cv2.threshold(diff, 15, 255, cv2.THRESH_TOZERO)

    diff_product = cv2.bitwise_and(diff, diff_old)

    # Image processing
    # diff = cv2.GaussianBlur(diff, (3, 3), 0)
    # ret, diff_thres = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)

    # diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)
    # diff_thres = cv2.erode(diff_thres, kernel, iterations=5)
    # diff_thres = cv2.dilate(diff_thres, kernel, iterations=5)

    # diff_total_product = cv2.multiply(diff, diff_1)
    # diff_total_product = cv2.multiply(diff_total_product, diff_2)

    # ret, diff_total_product = cv2.threshold(diff_total_product, 50, 255, cv2.THRESH_BINARY)

    # Display hard work
    cv2.imshow("gray_frame", gray_frame)
    cv2.imshow("diff", diff)
    # cv2.imshow("diff_product", diff_product)
    # cv2.imshow("diff_total_product", diff_total_product)

    # cv2.imshow("colored_frame", colored_frame)

    # Update the average frame
    gray_frame_avg = cv2.addWeighted(gray_frame_avg, 0.9, gray_frame, 0.1, 0)
    # diff_avg = cv2.addWeighted(diff_avg, 0.5, diff, 0.5, 0)

    diff_old = diff



    # Wait for escape key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()