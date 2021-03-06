import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import numpy as np

# Create a VideoCapture object
input_file = "WIN_20191129_14_32_31_Pro.mp4"
input_file_no_extension = os.path.splitext(input_file)[0]
cap = cv2.VideoCapture(input_file)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Unable to read camera feed")

# Prep led state
prev_led_on = False

save_clip = False
start_time = 0
end_time = 0

print("Searching for clips in the video...")
while (True):
    ret, frame = cap.read()
    if ret:
        # # Display the resulting frame
        # cv2.imshow('frame', frame)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(gray_frame[-1, -1], cap.get(cv2.CAP_PROP_POS_MSEC))

        if gray_frame[-1, -1] >= 128 and not prev_led_on:
            prev_led_on = True
            save_clip = True
            print("Turned on!")
        elif gray_frame[-1, -1] < 128 and prev_led_on:
            prev_led_on = False
            save_clip = True
            print("Turned off!")

        if save_clip:
            save_clip = False
            start_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000 - 3
            end_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000 + 3
            clip_name = input_file_no_extension + "_" + str(int(cap.get(cv2.CAP_PROP_POS_MSEC))) + ".mp4"
            ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=clip_name)

    # Break the loop
    else:
        break

# When everything done, release the video capture and video write objects
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

# Remove original file
os.remove(input_file)
print("Video Removed!")
