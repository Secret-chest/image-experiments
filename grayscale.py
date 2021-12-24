from PIL import Image, ImageShow

image = "sampleImages/EiffelTower.jpg"
viewImages = False

# Open image
with Image.open(image) as inputImage:
    # Reduce to 256 colors
    grayscaleImage = inputImage.convert("L")
    # Save
    grayscaleImage.save("grayscale/grayscale.png")

    if viewImages:
        ImageShow.show(grayscaleImage, "Dithering on")
