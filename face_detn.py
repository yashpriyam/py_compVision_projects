import cv2


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")       #searches for face in your image
                                                                            #more like an algorithm which verifies different parameters of your image and judges if its a face or not
img=cv2.imread("5.jpg")                 #using a grasyscale image helps recognise the image faster, as OpenCV is not very good software to recognise faces from images

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       #BGR2GRAY converts color to gray, we're only passsing the grey image to the function but we will have colored photo at the outpu
faces=face_cascade.detectMultiScale(gray_img,       #to draw a rectangle around a detected face
scaleFactor=1.25,           #number after the decimal shows in how many percentages python will divide the image to search for faces,
                            #smaller the number, higher the accuracy to detect a face
minNeighbors=5)             #tells python how many neighbors to search around the window

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)         #(x,y) co-ord of the top left corner,(x+w,y+h) co-ord of the bottom right corner
                                                                #(0,255,0,3) colors of the rectangle

print(type(faces))          #just for testing #prints the type of the function faces
print(faces)

resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))              #sometimes we may have an image that doesn't fits your window size, so we may want to resize it according to our window
#cv2.imshow("Gray",gray_img)
cv2.imshow("Gray",resized)          #passing the updated image 'img' or 'resized'
cv2.waitKey(0)
cv2.destroyAllWindows()
