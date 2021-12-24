from PIL import Image, ImageDraw, ImageShow

image = "sampleImages/AutunTheatreRomain.jpg"
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
            if g > r + 12 and g > b + 12:
                g = int(g * 1.12)
            b = int(b)
            draw.point((x, y), (r, g, b))

    recoloredImage.save("greenIntensify/intensified.png")

    if viewImages:
        ImageShow.show(recoloredImage, "Intensified green")
