import cv2

img_read1 = cv2.imread(r"C:\Users\Muhammad Yahya\Downloads\Computer_Vision\Open-Computer-Vision\Open-CV-14hrs\images\fruits.jpg")
img_read2 = cv2.imread(r"C:\Users\Muhammad Yahya\Downloads\Computer_Vision\Open-Computer-Vision\Open-CV-14hrs\images\smarties.png")

cv2.imshow("fresh fruits" , img_read1)
cv2.imshow("candies" , img_read2)

cv2.waitKey(0)

cv2.destroyAllWindows() #close all windows from backend

cv2.destroyWindow("smarties.png") #close particular window from backend  


# 5. Important Computer Vision Concepts.

# Function:	                Purpose:
# __________________________________________________________________
# cv2.imread()	            Image read karta hai
# cv2.imshow()	            Image display karta hai
# cv2.waitKey(0)	        Key press ka wait karta hai
# cv2.destroyAllWindows()	OpenCV ki windows close karta hai