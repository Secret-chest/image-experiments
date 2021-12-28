from PIL import Image, ImageShow

image = "sampleImages/DhaDhorm.jpg"
viewImages = False

# Open image
with Image.open(image) as inputImage:
    # Reduce to 216 colors
    ditheringOnImage = inputImage.convert("P")
    # Save
    ditheringOnImage.save("VGA/vgaDitheringOn.png")

    if viewImages:
        ImageShow.show(ditheringOnImage, "Dithering on")

    # Reduce to 216 colors
    ditheringOffImage = inputImage.convert("P", dither=Image.NONE)
    # Save
    ditheringOffImage.save("VGA/vgaDitheringOff.png")

    if viewImages:
        ImageShow.show(ditheringOffImage, "Dithering off")
