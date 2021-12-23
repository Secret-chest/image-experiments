from PIL import Image, ImageShow, ImagePalette
image = "sampleImages/EiffelTower.jpg"
viewImages = True

# Open image
with Image.open(image) as inputImage:
    # Reduce to black and white
    ditheredImage = inputImage.convert("1")
    # Save
    ditheredImage.save("dither/dithered.png")

    if viewImages:
        ImageShow.show(ditheredImage, "Dithered")
