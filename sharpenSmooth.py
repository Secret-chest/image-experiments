from PIL import Image, ImageShow, ImageFilter

image = "sampleImages/BotanicGarden.jpg"
viewImages = False

with Image.open(image) as inputImage:
    # Filter
    sharpenedImage = inputImage.filter(ImageFilter.SHARPEN)
    # Save
    sharpenedImage.save("sharpenSmooth/sharpened.png")

    if viewImages:
        ImageShow.show(sharpenedImage, "Sharpened")

    # Filter
    smoothedImage = inputImage.filter(ImageFilter.SMOOTH)
    # Save
    smoothedImage.save("sharpenSmooth/smoothed.png")

    if viewImages:
        ImageShow.show(smoothedImage, "Smoothed")

    # Filter
    smoothedImage2 = inputImage.filter(ImageFilter.SMOOTH_MORE)
    # Save
    smoothedImage2.save("sharpenSmooth/smoothedExtra.png")

    if viewImages:
        ImageShow.show(smoothedImage2, "More smoothed")
