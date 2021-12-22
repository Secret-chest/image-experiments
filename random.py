import numpy
from PIL import Image, ImageShow

imgWidth = 1280
imgHeight = 720

colorArray = numpy.random.rand(imgHeight, imgWidth, 3) * 255
colorImg = Image.fromarray(colorArray.astype("uint8")).convert("RGB")
colorImg.save("randomColors.bmp")

grayscaleArray = numpy.random.rand(imgHeight, imgWidth, 3) * 255
grayscaleImg = Image.fromarray(grayscaleArray.astype("uint8")).convert("L")
grayscaleImg.save("randomGrayscale.bmp")

ImageShow.show(grayscaleImg, "Grayscale")
ImageShow.show(colorImg, "Color")
