from PIL import Image, ImageShow, ImageFilter

image = "sampleImages/Hills.jpg"
viewImages = False

with Image.open(image) as inputImage:
    # Filter
    blurredImage = inputImage.filter(ImageFilter.BLUR)
    # Save
    blurredImage.save("blur/normalBlur.png")

    if viewImages:
        ImageShow.show(blurredImage, "Normal blur")

    # Filter
    blurredImage2 = inputImage.filter(ImageFilter.GaussianBlur(2))
    # Save
    blurredImage2.save("blur/gaussianBlur.png")

    if viewImages:
        ImageShow.show(blurredImage2, "Gaussian blur")

    # Filter
    blurredImage3 = inputImage.filter(ImageFilter.GaussianBlur(4))
    # Save
    blurredImage3.save("blur/gaussianBlurExtra.png")

    if viewImages:
        ImageShow.show(blurredImage3, "More Gaussian blur")

    # Filter
    blurredImage4 = inputImage.filter(ImageFilter.BoxBlur(3))
    # Save
    blurredImage4.save("blur/boxBlur.png")

    if viewImages:
        ImageShow.show(blurredImage4, "Box blur")

    # Filter
    blurredImage5 = inputImage.filter(ImageFilter.BoxBlur(6))
    # Save
    blurredImage5.save("blur/boxBlurExtra.png")

    if viewImages:
        ImageShow.show(blurredImage5, "More box blur")
