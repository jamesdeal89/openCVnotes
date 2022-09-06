# reading video
import cv2

# video can be read using cv2.VideoCapture
# this is done in individual video frames being processed
# a webcam feed can be used by passing in 0 for the default webcam 
# a saved video file uses a string of the filepath
capture = cv2.VideoCapture('cat.mp4')

# using a loop we can iterate through frames
while True:
    # .read() returns a tuple of a boolean and the image frame
    isTrue, frame = capture.read()
    # if there is a frame
    if isTrue:
        # display the frame
        cv2.imshow('video',frame)
    # wait for any keypress and stop if so
    if cv2.waitKey(0):
        break
# stops loading video
capture.release()
cv2.destroyAllWindows()
