import cv2

cap = cv2.VideoCapture(2)
print(cap.get(cv2.CAP_PROP_CONTRAST))
print(cap.get(cv2.CAP_PROP_EXPOSURE))
cap.set(cv2.CAP_PROP_CONTRAST, 32)  # 32
cap.set(cv2.CAP_PROP_EXPOSURE, -6)  # -6
print(cap.get(cv2.CAP_PROP_CONTRAST))
print(cap.get(cv2.CAP_PROP_EXPOSURE))
print(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("test.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)

    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)

    # Wait for escape key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
