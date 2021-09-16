import cv2
import numpy as np
import matplotlib.pylab as plt
img = cv2.imread("20030001_PhamVanKhoa_A1.jpg")
cv2.imshow("Origin", img)
img_contour = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_Blur = cv2.GaussianBlur(img_gray,(5,5),1)
img_canny = cv2.Canny(img_Blur,10,50)
contours,_ = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img_contour, contours, -1,(0,255,0),1)

cv2.imshow("Blur", img_Blur)
cv2.imshow("Canny",img_canny)

def rect_Contour(contours):
    for i in contours:
        area = cv2.arcLength(i,True)
        
rect_Contour(contours)

cv2.waitKey(0)
cv2.destroyAllWindows()