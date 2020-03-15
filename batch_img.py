import cv2
import glob

images=glob.glob("*.jpg")       #glob finds the files named with a certain pattern.in this ccase all files with jpg extension

for image in images:
    img=cv2.imread(image,0)     #'imread' function loads image in python #0 for all images to be in grayscale
    re=cv2.resize(img,(427,355))
    cv2.imshow("hey",re)            #re lets you checkout the images that are being resized
    cv2.waitKey(0)                      #'waitkey' function helps you decide how long thr=e imagewindow stays open
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)          #will add the word "resize" to the file name which has been resized
                                                #new resized image is created in the directory
