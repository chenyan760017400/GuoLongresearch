import cv2
import numpy as np

img=cv2.imread("Resources/cards.jpg")

width,height=250,350
pts1=np.float32([[111,219],[287,188],[154,482],[352,410]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imageoutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("output",imageoutput)
cv2.imwrite("one card.png",imageoutput)

cv2.waitKey(0)