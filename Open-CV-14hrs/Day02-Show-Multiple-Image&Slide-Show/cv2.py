import cv2

im_read = cv2.imread(r"C:\Users\Muhammad Yahya\Downloads\Computer_Vision\Open-Computer-Vision\Open-CV-14hrs\images\fruits.jpg")

cv2.imshow("juicy" , im_read)

cv2.waitKey(0)

cv2.destroyAllWindows()