import cv2
#get img loc and img file
img_location = 'C:/Users/ameya/OneDrive/Desktop/'
filename = 'download.jpeg'
#read the img
img = cv2.imread(img_location+filename)
#convert the img to greyscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#invert the img
inverted_gray_image = 250 - gray_image
#blur the img by using gaussian function
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0) 
#invert the blur img
inverted_blurred_img = 250 - blurred_img
#create the pencil sketch
pencil_sketch_img = cv2.divide(gray_image, inverted_blurred_img, scale=200.0)
#show the img
cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_img)
cv2.waitKey(0)


