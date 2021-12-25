from PIL import Image, ImageShow

image = "sampleImages/Dahlia.jpg"
viewImages = True

with Image.open(image) as inputImage:
    # Get size
    imageSizeX4 = (inputImage.size[0] * 4, inputImage.size[1] * 4)

    # Upscale
    upscaledNearest = inputImage.resize(imageSizeX4, resample=Image.NEAREST)
    upscaledBox = inputImage.resize(imageSizeX4, resample=Image.BOX)
    upscaledBilinear = inputImage.resize(imageSizeX4, resample=Image.BILINEAR)
    upscaledHamming = inputImage.resize(imageSizeX4, resample=Image.HAMMING)
    upscaledBicubic = inputImage.resize(imageSizeX4, resample=Image.BICUBIC)
    upscaledLanczos = inputImage.resize(imageSizeX4, resample=Image.LANCZOS)

    # Save
    upscaledNearest.save("upscale/upscaledNearest.png")
    upscaledBox.save("upscale/upscaledBox.png")
    upscaledBilinear.save("upscale/upscaledBilinear.png")
    upscaledHamming.save("upscale/upscaledHamming.png")
    upscaledBicubic.save("upscale/upscaledBicubic.png")
    upscaledLanczos.save("upscale/upscaledLanczos.png")

    # View
    if viewImages:
        ImageShow.show(upscaledNearest, "Nearest")
        ImageShow.show(upscaledBox, "Box")
        ImageShow.show(upscaledBilinear, "Bilinear")
        ImageShow.show(upscaledHamming, "Hamming")
        ImageShow.show(upscaledBicubic, "Bicubic")
        ImageShow.show(upscaledLanczos, "Lanczos")
