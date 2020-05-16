import cv2
import numpy as np 

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (250,0), (500, 250), (255, 255, 255), -1)

bitAnd = cv2.bitwise_and(img1, img2)
    #black -> 0 : white -> 1

bitOr = cv2.bitwise_or(img1, img2)

bitNot = cv2.bitwise_not(img1)

bitXor = cv2.bitwise_xor(img1, img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
#cv2.imshow("bitAnd", bitAnd)
#cv2.imshow("bitOr", bitOr)
#cv2.imshow("bitNot", bitNot)
cv2.imshow("bitXor", bitXor)


k = cv2.waitKey(0) & 0xFF
if k == 27 |ord('q'):
    cv2.destroyAllWindows()