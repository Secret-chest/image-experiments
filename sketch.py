from PIL import Image, ImageShow, ImageFilter

image = "sampleImages/PalmTree.jpg"
viewImages = False
cleanup = 0.7

with Image.open(image) as inputImage:
    # Filter
    sketchImage = inputImage.filter(ImageFilter.GaussianBlur(cleanup))
    sketchImage = sketchImage.filter(ImageFilter.CONTOUR)
    sketchImage = sketchImage.convert("L")
    # Save
    sketchImage.save("sketch/sketch.png")

    if viewImages:
        ImageShow.show(sketchImage, "Sketch")
