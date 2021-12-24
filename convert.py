from PIL import Image
from pathlib import Path

image = "sampleImages/AutunTheatreRomain.jpg"

with Image.open(image) as inputImage:
    originalName = Path(image).stem
    inputImage.save("convert/" + originalName + ".png")
    inputImage.save("convert/" + originalName + ".jpg")
    inputImage.save("convert/" + originalName + ".gif")
    inputImage.save("convert/" + originalName + ".bmp")
    inputImage.save("convert/" + originalName + ".webp")
    inputImage.save("convert/" + originalName + ".tiff")
