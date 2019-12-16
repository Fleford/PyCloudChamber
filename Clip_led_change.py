import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture("cut.mp4")

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Unable to read camera feed")

# Prep led state
prev_led_on = False
start_time = 0
end_time = 0


while (True):
    ret, frame = cap.read()

    if ret == True:
        # # Display the resulting frame
        # cv2.imshow('frame', frame)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(gray_frame[-1, -1], cap.get(cv2.CAP_PROP_POS_MSEC))

        if gray_frame[-1, -1] >= 128 and not prev_led_on:
            prev_led_on = True
            print("Turned on!")
        elif gray_frame[-1, -1] < 128 and prev_led_on:
            prev_led_on = False
            print("Turned off!")
            start_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000 - 3
            end_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000 + 3
            ffmpeg_extract_subclip("cut.mp4", start_time, end_time, targetname="cut_clip.mp4")

        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

    # When everything done, release the video capture and video write objects
cap.release()

# Closes all the frames
cv2.destroyAllWindows()


