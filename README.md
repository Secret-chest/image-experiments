# image-experiments
Image experiments made with Pillow

* randomImages.py - generate, with the given resolution:
  * randomColors.bmp - random RGB (True Color) pixels
  * randomGrayscale.bmp - random grayscale pixels
  * randomColorAlpha.png - random RGB pixels with alpha (transparency)
  * randomGrayscaleAlpha.png - random grayscale pixels with alpha (transparency)
  * random8bit.png - random 8-bit/VGA-supported/web-safe RGB pixels (all hexadecimal component colors are multiples of 33)
* dither.py - convert image to 1-bit (black _or_ white) for each pixel, and use dithering to give the illusion of more gray shades

<img src="https://user-images.githubusercontent.com/74449186/147381511-75d1d1ec-fab9-4efa-aa3a-65eb3645d9c4.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147381515-31df5926-2932-4282-99c0-cec6cef99f20.png" height=300px>

* VGA.py - convert image to 8-bit web colors, VGA-compatible, both with and without dithering

<img src="https://user-images.githubusercontent.com/74449186/147381543-1df08be7-efe3-4ea5-8a95-429c31d74fa7.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147381549-be59002d-1322-4b18-a7f4-6e1e46a693e1.png" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147381553-e044cf64-fdab-4e31-91f2-78273683a9fe.png" height=300px>

* grayscale.py - convert image to 8-bit grayscale

<img src="https://user-images.githubusercontent.com/74449186/147381635-10dcadc9-3cd5-4de8-b59f-7022754e9016.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147381637-539c7192-4622-4e96-8d0d-c9679c40b8c4.png" height=300px>

* sketch.py - generate:
  * sketch1.png - contour image with no line cleanup
  * sketch2.png - contour image with moderate line cleanup
  * sketch3.png - contour image with high line cleanup

<img src="https://user-images.githubusercontent.com/74449186/147382030-87b65957-ddcc-44f2-ad00-17b78511d3e9.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147381978-1b0a2672-7047-42ef-a3b2-cf9c49839c3f.png" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147381984-bed4d7df-e82c-4e8b-91fe-4faf4d167377.png" height=300px> <img src=https://user-images.githubusercontent.com/74449186/147381993-57c9a1a6-ac97-42d7-8dde-2047d8f4ffee.png height=300px>

* blur.py - generate:
  * normalBlur.png - default harsh blur
  * boxBlur.png - box blur
  * boxBlurExtra.png - more box blur
  * gaussianBlur.png - Gaussian blur
  * gaussianBlurExtra.png - more Gaussian blur

<img src="https://user-images.githubusercontent.com/74449186/147382060-237299f2-d843-4a0f-87c4-405d225b205e.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382114-8b04ebff-44a5-4e65-8b2a-8187fc737214.png" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382185-d7a27e4c-6b18-4989-bd4e-3aa7ae1627ef.png" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382208-77e20d45-6ebd-4417-bde1-91c9cdf9cd0b.png" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382236-e52d8a6d-939a-4cf9-a5a3-b59012f18437.png" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382254-295e3e54-c849-440e-8b39-cf8a0223fb39.png" height=300px>

* upscale.py - upscale image to 4x size using various algorithms
* convert.py - convert to various file formats
* hell.py - make all colors hot

<img src="https://user-images.githubusercontent.com/74449186/147382292-a16dd842-b017-463b-b106-ef05a17fbdfa.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382304-ff6711a5-c3d3-4241-91a2-1e1596d262de.png" height=300px>

* heaven.py - recolor image to a sky-blue shade

<img src="https://user-images.githubusercontent.com/74449186/147382325-47f33348-70e6-4c3d-9e81-aa8c5a031be7.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382352-9653f472-2081-4796-8c86-6b73f76f3593.png" height=300px>

* greenIntensify.py - intensify and optimize green hues, useful for images with vegetation

<img src="https://user-images.githubusercontent.com/74449186/147382372-0d19a904-ac3e-450d-946f-849bbdf45867.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382381-d05e94c0-6c36-40da-82f0-bc1940351936.png" height=300px>

* blueIntensify.py - intensify blue shades, making sky and water bluer

<img src="https://user-images.githubusercontent.com/74449186/147382397-b72ec737-8689-4ddd-97c5-0d57e611c2e6.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382418-1e28bc75-5877-45c6-a852-55b1269bcc69.png" height=300px>

* aqua.py - make images look underwater

<img src="https://user-images.githubusercontent.com/74449186/147382463-a6f8b0b2-f982-4704-be1f-70c6dec1006f.jpg" height=300px> <img src="https://user-images.githubusercontent.com/74449186/147382501-cc51880e-6b72-4940-a420-42d50fa221af.png" height=300px>

* sharpen.py/smooth.py - sharpen/smooth image contours
* colorPop.py - make pixels not in the set color range grayscale or transparent. I can't show transparent mode since I have no perfect image to use for it.

<img src="https://user-images.githubusercontent.com/74449186/147392168-6373f343-4c8f-43fb-a002-8474f1075e50.jpg" height=300px>
<img src="https://user-images.githubusercontent.com/74449186/147392141-a91b60c9-c1d1-4bff-a353-ad241c84e0af.png" height=300px> 



Each script generates files in a directory with the same name as the script, to avoid flooding the root directory.

For photo attribution, check the ATTRIBUTION.md file.
