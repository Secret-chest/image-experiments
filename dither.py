from PIL import Image, ImageShow, ImagePalette
image = "sampleImages/EiffelTower.jpg"
viewImages = True

CGA = ImagePalette.ImagePalette(mode="RGB", palette=((255, 255, 255, 0, 0, 0)))

# Open image
with Image.open(image) as inputImage:
    # Reduce to black and white
    ditheredImage = inputImage.convert("1")
    # Save
    ditheredImage.save("dither/dithered.png")

    if viewImages:
        ImageShow.show(ditheredImage, "Dithered")
