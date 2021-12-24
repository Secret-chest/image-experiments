from PIL import Image, ImageShow, ImageFilter

image = "sampleImages/PalmTree.jpg"
viewImages = False

with Image.open(image) as inputImage:
    # Filter
    sketchImage = inputImage.filter(ImageFilter.GaussianBlur(0))
    sketchImage = sketchImage.filter(ImageFilter.CONTOUR)
    sketchImage = sketchImage.convert("L")
    # Save
    sketchImage.save("sketch/sketch1.png")

    if viewImages:
        ImageShow.show(sketchImage, "Sketch")

    # Filter
    sketchImage = inputImage.filter(ImageFilter.GaussianBlur(0.75))
    sketchImage = sketchImage.filter(ImageFilter.CONTOUR)
    sketchImage = sketchImage.convert("L")
    # Save
    sketchImage.save("sketch/sketch2.png")

    if viewImages:
        ImageShow.show(sketchImage, "Sketch")

    # Filter
    sketchImage = inputImage.filter(ImageFilter.GaussianBlur(1))
    sketchImage = sketchImage.filter(ImageFilter.CONTOUR)
    sketchImage = sketchImage.convert("L")
    # Save
    sketchImage.save("sketch/sketch3.png")

    if viewImages:
        ImageShow.show(sketchImage, "Sketch")
