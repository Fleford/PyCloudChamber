import cv2

cap = cv2.VideoCapture("trace_cap_third.avi")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)

    # Wait for escape key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()