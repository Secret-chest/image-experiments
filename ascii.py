from PIL import Image, ImageEnhance

image = "sampleImages/WaterDrop.jpg"
characters = ["#", "0", "&", "@", "%", "u", "[", "i", "(", "1", "=", "+", "<", "|", "/", "!", "*", "^", ";", ":", "~", "_", "-", ",", "'", ".", "`", " "]
newWidth = 80
darkMode = True

with Image.open(image) as inputImage:
    width, height = inputImage.size
    aspectRatio = height / width
    newHeight = aspectRatio * newWidth * 0.38
    inputImage = inputImage.resize((newWidth, int(newHeight)))

    # If dark mode, reverse the list of characters
    if darkMode:
        characters.reverse()

    # Brighten the image and increase contrast
    inputImage = inputImage.convert("RGB")
    brightnessEnhancer = ImageEnhance.Brightness(inputImage)
    inputImage = brightnessEnhancer.enhance(2)
    contrastEnhancer = ImageEnhance.Contrast(inputImage)
    inputImage = contrastEnhancer.enhance(2)

    pixels = inputImage.getdata()

    # Map lightness to characters
    imageString = [characters[(pixel[0] + pixel[1] + pixel[2]) // len(characters)] for pixel in pixels]
    imageString = "".join(imageString)

    # Split string into rows
    length = len(imageString)
    imageText = [imageString[index:index + newWidth] for index in range(0, length, newWidth)]
    imageText = "\n".join(imageText)
    print(imageText)

    # Save a text file
    outputFile = open("ascii/ascii.txt", "w")
    outputFile.write(imageText)
