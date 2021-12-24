from PIL import Image, ImageDraw, ImageShow

image = "sampleImages/Sky.jpg"
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
            r = int(r)
            g = int(g)
            if b > r + 12 and b > g + 12:
                b = int(b * 1.12)
            draw.point((x, y), (r, g, b))

    recoloredImage.save("blueIntensify/intensified.png")

    if viewImages:
        ImageShow.show(recoloredImage, "Intensified blue")
