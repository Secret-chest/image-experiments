from PIL import Image, ImageShow, ImageFilter

image = "sampleImages/Hills.jpg"
viewImages = False
blurMode = "box"  # "box", "gaussian" or "default"
blurRadius = 6

with Image.open(image) as inputImage:
    if blurMode == "default":
        # Filter
        blurredImage = inputImage.filter(ImageFilter.BLUR)
        # Save
        blurredImage.save("blur/blurred.png")

        if viewImages:
            ImageShow.show(blurredImage, "Default blur")

    if blurMode == "box":
        # Filter
        blurredImage = inputImage.filter(ImageFilter.BoxBlur(blurRadius))
        # Save
        blurredImage.save("blur/blurred.png")

        if viewImages:
            ImageShow.show(blurredImage, "Box blur")

    if blurMode == "gaussian":
        # Filter
        blurredImage = inputImage.filter(ImageFilter.GaussianBlur(blurRadius))
        # Save
        blurredImage.save("blur/blurred.png")

        if viewImages:
            ImageShow.show(blurredImage, "Gaussian blur")
