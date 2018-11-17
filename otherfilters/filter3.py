from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import sys

img = Image.open(sys.argv[1])
width, height = img.width, img.height
img = ImageOps.posterize(img, 4)

r = img.split()[0]
r = ImageEnhance.Contrast(r).enhance(2.0)
r = ImageEnhance.Brightness(r).enhance(1.5)
r = ImageOps.colorize(r, (0,0,255), (255,0,255))

img = Image.blend(img, r, 0.55)
img = ImageEnhance.Sharpness(img).enhance(20.0)

img.save("filter10.jpg")