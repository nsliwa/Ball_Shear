import cv2
image = cv2.imread('test_image.png')
image2 = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY, 
    )
image2 = cv2.GaussianBlur(
    image2, 
    ksize=(9,9), 
    sigmaX=8,
    sigmaY=8,
    )
cv2.imwrite('blurred.png', image2)
hello, image2 = cv2.threshold(
    image2,
    thresh=95,
    maxval=255,
    type=cv2.THRESH_BINARY_INV,
    )
cv2.imwrite('thresholded.png', image2)
contours, hier = cv2.findContours(
    image2,  # Note: findContours() changes the image.
    mode=cv2.RETR_EXTERNAL,
    method=cv2.CHAIN_APPROX_NONE,
    )
print('Number of contours: {0}'.format(len(contours)))
cv2.drawContours(
    image,
    contours=contours,
    contourIdx=-1,
    color=(0,255,0),
    thickness=2,
    )
cv2.imwrite('augmented.png', image)
cv2.imshow('hello', image)
cv2.waitKey(-1)
