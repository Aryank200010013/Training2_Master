import numpy as np
import cv2

cam_x=1920
cam_y=1080
k=0.86
find=0
d=0


img = cv2.imread('frame_-0.230.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th1 = cv2.threshold(img2, 30 , 255, cv2.THRESH_BINARY)
cv2.line(th1, (-110,10), (2010,10), (0, 0, 0), 700, cv2.LINE_AA)
cv2.line(th1, (-110,1070), (2010,1070), (0, 0, 0), 700, cv2.LINE_AA)

contours,_ = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.0105* cv2.arcLength(contour, True), True)
    cv2.drawContours(th1, [approx], 0, (0, 0, 0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] 
    if len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        #print(x)
        #print(y)
        pos=int(x+w/2)-int(cam_x/2)
        find=pos
        print(pos)
        area=w*h
        print(area)
        print( )

        #cv2.putText(th1, ("("+str(x)+","+str(y)+")"), (int(x+w/2), int(y+h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (160, 0, 0), 2)
        cv2.putText(th1, (str(pos)), (int(x+w/2)-35, int(y+h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0), 2)


d=2.0*k*float(pos)/float(cam_x)+0.5
print(d)
print()


cv2.imwrite('output.jpg',th1)
cv2.imshow("window1", th1)

cv2.waitKey(10000)