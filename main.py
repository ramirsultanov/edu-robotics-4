import cv2
import numpy as np
import random as rnd

image = cv2.imread("resources/input.png")

cv2.imshow("original", image)

# Noising image
noised = image
level = 0.1
for i in range(noised.shape[0]):
    for j in range(noised.shape[1]):
        if rnd.random() < level:
            if rnd.randint(0, 1) == 0:
                noised[i][j] = 0
            else:
                noised[i][j] = 255
cv2.imshow("noised", noised)

# Averaging filtering
averaged_size = 3
averaged = cv2.blur(noised, (averaged_size, averaged_size))
cv2.imshow("averaged", averaged)

# Median filtering
median_size = 3
medianed = cv2.medianBlur(noised, median_size)
cv2.imshow("medianed", medianed)

# Gaussian blur
gaussian_size = 5
sigmaX = 0
sigmaY = 0
gaussianned = cv2.GaussianBlur(noised, (gaussian_size, gaussian_size), sigmaX, sigmaY)
cv2.imshow("gaussianned", gaussianned)

# Bilateral filtering
bilateral_d = 9
sigmaColor = 100
sigmaSpace = 100
billateralled = cv2.bilateralFilter(noised, bilateral_d, sigmaColor, sigmaSpace)
cv2.imshow("bilateralled", billateralled)

cv2.waitKey(0)
