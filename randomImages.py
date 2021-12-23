import numpy
from PIL import Image, ImageShow

imgWidth = 1280
imgHeight = 720
viewImages = False

# True color
colorArray = numpy.random.rand(imgHeight, imgWidth, 3) * 256
colorImg = Image.fromarray(colorArray.astype("uint8")).convert("RGB")
colorImg.save("randomImages/randomColors.bmp")

# 8-bit colors
color8bitArray = numpy.random.rand(imgHeight, imgWidth, 3) * 256
color8bitImg = Image.fromarray(color8bitArray.astype("uint8")).convert("P")
color8bitImg.save("randomImages/random8bit.bmp")

# True color with transparency
colorAlphaArray = numpy.random.rand(imgHeight, imgWidth, 4) * 256
colorAlphaImg = Image.fromarray(colorAlphaArray.astype("uint8")).convert("RGBA")
colorAlphaImg.save("randomImages/randomColorAlpha.png")

# Grays
grayscaleArray = numpy.random.rand(imgHeight, imgWidth, 3) * 256
grayscaleImg = Image.fromarray(grayscaleArray.astype("uint8")).convert("L")
grayscaleImg.save("randomImages/randomGrayscale.bmp")

# Grays with transparency
grayscaleAlphaArray = numpy.random.rand(imgHeight, imgWidth, 4) * 256
grayscaleAlphaImg = Image.fromarray(grayscaleAlphaArray.astype("uint8")).convert("LA")
grayscaleAlphaImg.save("randomImages/randomGrayscaleAlpha.png")

# Black and white
blackWhiteArray = numpy.random.rand(imgHeight, imgWidth, 3) * 256
blackWhiteImg = Image.fromarray(blackWhiteArray.astype("uint8")).convert("1")
blackWhiteImg.save("randomImages/randomBlackWhite.bmp")

if viewImages:
    ImageShow.show(grayscaleImg, "Grayscale")
    ImageShow.show(colorImg, "Color")
    ImageShow.show(blackWhiteImg, "Black/White")
    ImageShow.show(grayscaleAlphaImg, "Grayscale w/ alpha")
    ImageShow.show(colorAlphaImg, "Black/White w/ alpha")
    ImageShow.show(color8bitImg, "8-bit color")
