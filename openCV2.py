# reading video
import cv2

# video can be read using cv2.VideoCapture
# this is done in individual video frames being processed
# a webcam feed can be used by passing in 0 for the default webcam 
# a saved video file uses a string of the filepath
capture = cv2.VideoCapture('cat.mp4')

# get the first frame
isTrue, frame = capture.read()
# resize the frame 
frame = cv2.resize(frame,(600,400))

# using a loop we can iterate through frames if the first frame was succesful
while isTrue:
    # display the frame
    cv2.imshow('video',frame)
    # get next frame
    isTrue, frame = capture.read()
    # resize next frame 
    frame = cv2.resize(frame,(600,400))
    # wait for any keypress and stop if so
    if cv2.waitKey(0):
        break
# stops loading video
capture.release()
cv2.destroyAllWindows()


