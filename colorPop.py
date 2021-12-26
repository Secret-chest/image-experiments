from PIL import Image, ImageDraw, ImageShow
from colorsys import rgb_to_hls, hls_to_rgb

image = "sampleImages/Clementines.jpg"
viewImages = False
colorHues = [(0, 179)]
colorLightness = (0, 80)
colorSaturation = (3, 100)
backgroundMode = "transparent"  # you can change this to "transparent" or "grayscale"

# Open image
with Image.open(image) as inputImage:
    inputPixels = inputImage.load()

    if backgroundMode == "grayscale":
        # Create output image
        recoloredImage = Image.new("RGBA", inputImage.size)
        draw = ImageDraw.Draw(recoloredImage)

        # Recolor each pixel and draw it
        for x in range(recoloredImage.width):
            for y in range(recoloredImage.height):
                r, g, b = inputPixels[x, y]

                # get hue and lightness in full integer format
                hue = round(rgb_to_hls(r / 255, g / 255, b / 255)[0] * 360)
                lightness = round(rgb_to_hls(r / 255, g / 255, b / 255)[1] * 100)
                saturation = round(rgb_to_hls(r / 255, g / 255, b / 255)[2] * 360)

                # assume we don't draw the color, most pixels won't be colored
                drawColor = False

                if colorLightness[0] < lightness < colorLightness[1] and colorSaturation[0] < saturation < colorSaturation[1]:
                    for colorHue in colorHues:
                        if colorHue[0] > colorHue[1]:
                            if colorHue[0] < hue or hue < colorHue[1]:
                                drawColor = True
                        else:
                            if colorHue[0] < hue < colorHue[1]:
                                drawColor = True
                if not drawColor:
                    shade = round(lightness / 100 * 255)
                    r, g, b = shade, shade, shade

                draw.point((x, y), (r, g, b))

        recoloredImage.save("colorPop/pop.png")

        if viewImages:
            ImageShow.show(recoloredImage, "Color pop")

    elif backgroundMode == "transparent":
        # Create output image
        transparentImage = Image.new("RGBA", inputImage.size, color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(transparentImage)

        # Recolor each pixel and draw it
        for x in range(transparentImage.width):
            for y in range(transparentImage.height):
                r, g, b = inputPixels[x, y]

                # get hue and lightness in full integer format
                hue = round(rgb_to_hls(r / 255, g / 255, b / 255)[0] * 360)
                lightness = round(rgb_to_hls(r / 255, g / 255, b / 255)[1] * 100)
                saturation = round(rgb_to_hls(r / 255, g / 255, b / 255)[2] * (100 / 3.6))

                # assume we don't draw the color, most pixels won't be colored
                drawColor = False

                if colorLightness[0] < lightness < colorLightness[1] and colorSaturation[0] < saturation < colorSaturation[1]:
                    for colorHue in colorHues:
                        if colorHue[0] > colorHue[1]:
                            if colorHue[0] < hue or hue < colorHue[1]:
                                drawColor = True
                        else:
                            if colorHue[0] < hue < colorHue[1]:
                                drawColor = True
                if drawColor:
                    draw.point((x, y), (r, g, b))

        transparentImage.save("colorPop/popTransparent.png")

        if viewImages:
            ImageShow.show(transparentImage, "Transparent color pop")
