from PIL import Image, ImageDraw, ImageShow

image = "sampleImages/AvenueDesChamps.jpg"
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
            r = int((r + 144) // 1.2)
            g = int((g // 4 + 64) // 1.7)
            b = int((b // 2) // 2)
            draw.point((x, y), (r, g, b))

    recoloredImage.save("hell/hell.png")

    if viewImages:
        ImageShow.show(recoloredImage, "Hell")
