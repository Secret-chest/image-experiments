# image-experiments
Image experiments made with Pillow

* randomImages.py - generate with the given resolution:
  * randomColors.bmp - random RGB (True Color) pixels
  * randomGrayscale.bmp - random grayscale pixels
  * randomColorAlpha.png - random RGB pixels with alpha (transparency)
  * randomGrayscaleAlpha.png - random grayscale pixels with alpha (transparency)
  * random8bit.png - random 8-bit/VGA-supported/web-safe RGB pixels (all hexadecimal component colors are multiples of 33)
* dither.py - convert image to 1-bit (black _or_ white) for each pixel, and use dithering to give the illusion of more gray shades
* VGA.py - convert image to 8-bit web colors, VGA-compatible, both with and without dithering
* grayscale.py - convert image to 8-bit grayscale
* sketch.py - generate:
  * sketch1.png - contour image with no line cleanup
  * sketch2.png - contour image with moderate line cleanup
  * sketch3.png - contour image with high line cleanup
* blur.py - generate:
  * normalBlur.png - default harsh blur
  * boxBlur.png - box blur
  * boxBlurExtra.png - more box blur
  * gaussianBlur.png - Gaussian blur
  * gaussianBlurExtra.png - more Gaussian blur

Each script generates files in a directory with the same name, to avoid flooding the root directory.

For photo attribution, check the ATTRIBUTION.md file.
