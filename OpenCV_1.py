import cv2

img=cv2.imread("123.jpg",0)  #the argument after comma renders how you want to render the image, the colour background and all those things
#img=cv2.imread("123.jpg",1)     # 1 is passed if you want the image as it is
                                #0 for grayscale image
                                #-1 colour image
print(type(img))
print(img)          #displays the numpy array of pixels
print(img.shape)
print(img.ndim)     #python stores image as a numpy array

#resized_image=cv2.resize(img,(500,500))     # img,(width,height)  #resizing the image or inturn the numpy array, according to your wish
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Yash",resized_image)       #to display the image on screen ("title of the window")
cv2.imwrite("123_resized.jpg",resized_image)
cv2.waitKey(0)       #defines time in which the window will be closed, #(0) means press any button, window closes, (2000) means window closes if a button is pressed for 2000ms or 2s
cv2.destroyAllWindows()
