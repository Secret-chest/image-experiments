from PIL import Image, ImageShow

image = "sampleImages/Chicago.jpg"
viewImages = False

# Open image
with Image.open(image) as inputImage:
    # Reduce to black and white
    ditheredImage = inputImage.convert("1")
    # Save
    ditheredImage.save("dither/dithered.bmp")

    if viewImages:
        ImageShow.show(ditheredImage, "Dithered")
