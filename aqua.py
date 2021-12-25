from PIL import Image, ImageDraw, ImageShow

image = "sampleImages/Hummingbird.jpg"
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
            r = int(r // 1.5)
            g = int(g // 2 + 64)
            b = int(b + 192)
            draw.point((x, y), (r, g, b))

    recoloredImage.save("aqua/aqua.png")

    if viewImages:
        ImageShow.show(recoloredImage, "Aqua")
