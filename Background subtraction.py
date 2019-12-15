import cv2
import numpy as np

kernel = np.ones((2, 2), np.uint8)
bigger_kernel = np.ones((2, 2), np.uint8)
cap = cv2.VideoCapture(2)
ret, frame = cap.read()


fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=10, detectShadows=False)
fgmask = fgbg.apply(frame)

fgmask_old = fgmask
fgmask_older = fgmask_old
fgmask_olderer = fgmask_older
fgmask_oldererer = fgmask_olderer

cnt_avg = 0.

all_zeros = cv2.bitwise_not(fgmask * 0)
colored_blank = cv2.applyColorMap(all_zeros, cv2.COLORMAP_HSV)

# Vid capture test
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("colored_traces1.avi", fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()

    # Extract traces
    fgmask = fgbg.apply(frame)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    # fgmask = cv2.dilate(fgmask, bigger_kernel, iterations=1)
    mask = cv2.bitwise_and(fgmask, fgmask_old)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # mask = cv2.dilate(mask, kernel, iterations=1)
    # mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.bitwise_and(mask, fgmask_older)
    # mask = cv2.erode(mask, kernel, iterations=1)
    # mask = cv2.dilate(mask, kernel, iterations=1)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # mask = cv2.bitwise_and(mask, fgmask_olderer)
    # mask = cv2.erode(mask, kernel, iterations=1)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # mask = cv2.bitwise_and(mask, fgmask_oldererer)
    mask_inv = cv2.bitwise_not(mask)

    # Just the foreground
    fg_blanks = cv2.bitwise_and(colored_blank, colored_blank, mask=mask)

    # Just the background
    bg_image = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Put fg and bg together
    colored_frame = cv2.add(fg_blanks, bg_image)


    # Set current frame to old
    fgmask_oldererer = fgmask_olderer
    fgmask_olderer = fgmask_older
    fgmask_older = fgmask_old
    fgmask_old = fgmask

    # Count stuff
    if np.count_nonzero(mask) >= 3 * cnt_avg:
        print(np.count_nonzero(mask))
        # out.write(frame)

        # Display text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(colored_frame, 'Particle Detected!', (30, 90), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display hard work
    # cv2.imshow("mask", mask)
    # cv2.imshow("frame", frame)
    cv2.imshow("colored_frame", colored_frame)
    out.write(colored_frame)



    # Update average cnt
    cnt_avg = 0.99 * cnt_avg + 0.01 * np.count_nonzero(mask)


    # Wait for escape key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()