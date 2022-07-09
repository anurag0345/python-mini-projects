# Import OpenCV library for image handling
import cv2

# Read image to be resized by imread() function of openCV library
img = cv2.imread('astronaut.jpg')
print(img.shape)

# Set the ratio of resized image
k = 5
width = int((img.shape[1])/k)
height = int((img.shape[0])/k)

# Resize the image by resize() function of OpenCV library
scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
print(scaled.shape)

# Show the resized image using imshow() function of OpenCV library
cv2.imshow("Output", scaled)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# Get the resized image output by imwrite() function of OpenCV library
cv2.imwrite('resized_output_image.jpg', scaled)
