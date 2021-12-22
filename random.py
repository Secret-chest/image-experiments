import cv2
import numpy
from PIL import Image, ImageShow

imgWidth = 1280
imgHeight = 720

print(imgWidth * imgHeight * 256 ** 3)

colorArray = numpy.random.rand(imgHeight, imgWidth, 3) * 255
colorImg = Image.fromarray(colorArray.astype("uint8")).convert("RGB")
colorImg.save("randomColors.bmp")

grayscaleArray = numpy.random.rand(imgHeight, imgWidth, 3) * 255
grayscaleImg = Image.fromarray(grayscaleArray.astype("uint8")).convert("L")
grayscaleImg.save("randomGrayscale.bmp")

grayscaleImg = cv2.imread("randomGrayscale.bmp")
colorImg = cv2.imread("randomColors.bmp")

cv2.imshow("Grayscale", grayscaleImg)
cv2.imshow("Color", colorImg)
cv2.waitKey(0)
