from PIL import Image, ImageShow, ImageFilter

image = "sampleImages/BotanicGarden.jpg"
viewImages = False

with Image.open(image) as inputImage:
    # Filter
    sharpenedImage = inputImage.filter(ImageFilter.SHARPEN)
    # Save
    sharpenedImage.save("sharpen/sharpened.png")

    if viewImages:
        ImageShow.show(sharpenedImage, "Sharpened")
