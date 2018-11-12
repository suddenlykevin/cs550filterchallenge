from PIL import Image, ImageEnhance
import PIL
import sys

image = Image.open(sys.argv[1])
pixels = image.load()
w, h = image.size

for x in range(w):
	for y in range(h):
		r, g, b = pixels[x,y]
		if r>=140:
			r+=1000
		if g>=100:
			g-=1000
			b-=100
			r-=100
		if b>=10:
			b+=1000
		pixels[x,y] = (r,g,b)

image.save("filtered1.jpg")

# PIL.ImageChops.invert(image).save("filtered.jpg")