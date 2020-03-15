#when we start the video camera the first frame should capture a 'static' background so that it can compare moving objects with the static background and detect them
#this program detects a moving object and notes the time when the object entered the frame and when did it leave
#capture the first frame through the camera, and store it into a variable and then pass that variable into grayscale
import cv2, time, pandas                #'pandas' helps you print start time and end time in different coloumns   'time'helps you add stopwatch sort of functionality to your program
from datetime import datetime

first_frame=None                                #we need to store the first frame or the numpy array of the first frame in a variable
status_list=[None,None]                                #None is a python data type that allows you to create a variable and assign nothing to it
times=[]
df=pandas.DataFrame(columns=["Start","End"])
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)        #enables the camera, starts it #1 for external camera

while True:
    check, frame = video.read()                 #we will show each frame of the video being captured
    status=0                                    #add time to your video
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)     #converting the first frame,which is just an image, into a grayscale image
    gray=cv2.GaussianBlur(gray,(21,21),0)                         #to increase accuracy # it gets the parameter the image which you want to pass herre

    if first_frame is None:                         #when the video starts, and if the first frame has None means it is static nothing is moving in front of the camera
        first_frame=gray                            #if the first fraame is none, we assign it to gray
        continue                                    #if first frame is none then go the second frame, dont end the script

    delta_frame=cv2.absdiff(first_frame,gray)          #we're comparing the first frame and the current frame
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)           #to smooth the image, and reduce white area

    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)     #find contours in image and store them in python

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status=1

        (x, y, w, h)=cv2.boundingRect(contour)                                 #adding face detection to video
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)

    status_list=status_list[-2:]


    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())


    cv2.imshow("Gray frame",gray)   #python captures the video for 3 secs but shows in the window only the very first frame
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)               #if you dont press 'q' to quit, it continues to show videos in frames 1 frame after every 1000ms or 1s
#    print(gray)
#    print(delta_frame)

    if key==ord('q'):                                   #if you press 'q' the while loop breaks
        if status==1:
            times.append(datetime.now())          #adds the time when the button quit was pressed as the end time
        break

print(status_list)
print(times)#datetime.now()

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)         #adding the first datetime entry to start column and next[i+1] entry to end column

df.to_csv("Times.csv")                      #store the dataframe timing in a csv file in the same directory

video.release()             #stops video capturing
cv2.destroyAllWindows()
