import cv2

img =cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(0,0),fx=0.1,fy=0.1)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()