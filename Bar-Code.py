import cv2 as cv
import numpy as np
img=np.random.randint(0,2,(1,256)).astype("float32")*255. #generating 0 and 1 and multiplying by 255.
print(img)  #printitng value.....
img=cv.resize(img,(256,50))
cv.imwrite("BarCode.png",img)
cv.imshow("BarCode.png",img)
cv.waitKey(0)
cv.destroyAllWindows()