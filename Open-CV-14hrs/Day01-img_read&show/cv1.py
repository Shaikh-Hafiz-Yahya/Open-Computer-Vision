import cv2
from pathlib import Path

# Get current Python file directory
BASE_DIR = Path(__file__).resolve().parent

# Image path
image_path = BASE_DIR / "images" / "fruits.jpg"

# Read image
img = cv2.imread(str(image_path))

if img is not None:

    cv2.imshow("Displaying Image", img) # open the window

    cv2.waitKey(0) # ZERO = Hold Kro display image (press any key)

    cv2.destroyAllWindows() # backend sy image ko successfully remove (close the all windows)

else:
    print("Image Does Not Exist..")


# 5. Important Computer Vision Concepts.

# Function:	                Purpose:
# __________________________________________________________________
# cv2.imread()	            Image read karta hai
# cv2.imshow()	            Image display karta hai
# cv2.waitKey(0)	        Key press ka wait karta hai
# cv2.destroyAllWindows()	OpenCV ki windows close karta hai
# Path(__file__)	        Current Python file ka location deta hai
