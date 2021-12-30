from PIL import Image, ImageDraw, ImageShow

image = "sampleImages/Hills2.jpg"
viewImages = False

# Open image
with Image.open(image) as inputImage:
    inputPixels = inputImage.load()

    # Create output image
    recoloredImage = Image.new("RGBA", inputImage.size)
    draw = ImageDraw.Draw(recoloredImage)

    # Recolor each pixel and draw it
    for x in range(recoloredImage.width):
        for y in range(recoloredImage.height):
            r, g, b = inputPixels[x, y]
            r = int(r + 48)
            initialG = g
            g = int(g * 1.6 + 36)
            b = int(initialG + 84)
            draw.point((x, y), (r, g, b))

    recoloredImage.save("heaven/heaven.png")

    if viewImages:
        ImageShow.show(recoloredImage, "Heaven")
