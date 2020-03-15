import cv2, time                #helps you add stopwatch sort of fucctionality to your program

#video=cv2.VideoCapture(0)            #starts video capturing # '0' means you are capturing video using inbuilt webcam
#camera_port = 0
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)        #enables the camera, starts it #1 for external camera
a=0             #to check the frame rate
while True:
    a=a+1
    check, frame = video.read()                 #we will show each frame of the video being captured

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)     #converting the first frame,which is just an image, into a grayscale image
    #time.sleep(3)                   #waits for 5seconds before executing the next line
    cv2.imshow("Capturing",frame)   #python captures the video for 3 secs but shows in the window only the very first frame

    key=cv2.waitKey(1)               #if you dont press 'q' to quit, it continues to show videos in frames 1 frame after every 1000ms or 1s

    if key==ord('q'):               #if you press 'q' the while loop breaks
        break

print(a/key)                            #prints the frames per second
video.release()             #stops video capturing
cv2.destroyAllWindows()
