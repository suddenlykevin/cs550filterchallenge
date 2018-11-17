"""
Halftoning
Kevin Xie CS550
Healey

Halftoning algorithm was heavily adapted and simplified from: 
https://stackaoverflow.com/questions/10572274/halftone-images-in-python
However, I made an effort to understand everything before I typed it.
He/she was using all CMYK channels, offsetting, and merging, but I just
wanted to halfshade one channel. Also, he/she seemed to be working in
Python 2 or lower, since some of the commands could be simplified.
The rest of the colorization was my choice.

Sources:
Halftoning - https://stackaoverflow.com/questions/10572274/halftone-images-in-python

On My Honor, I have neither given nor received unauthorized aid.
Kevin Xie 
"""

from PIL import Image, ImageDraw, ImageStat, ImageFilter, ImageOps, ImageEnhance
import sys

# domain/size of each halftoned "circle" -- determines final "circle resolution" 
sample = 30 
# takes B channel of new image
im = Image.open(sys.argv[1]) 
channel = im.split()[2]
# New, single 8-bit channel image for halftoning
halftoned = Image.new('L', (channel.width,channel.height)) 
# sets the draw command
draw = ImageDraw.Draw(halftoned) 
# goes from 0 to width of image with step size of 30 (sample size -- basically in a grid of width/30)
for x in range(0, channel.width, sample): 
    for y in range(0, channel.height, sample): 
    	# makes a new box that takes a sample sized (30x30) square of the original image's B channel
        box = channel.crop((x, y, x + sample, y + sample)) 
        # sets the stat command
        stat = ImageStat.Stat(box) 
        # Scales diameter of the halftoning circle (0-sample=30) based on the 0-255 value of the L (only) channel which indicates pixel brightness out of 255 to make it a value from 0-1
        diameter = stat.mean[0]*sample / 255 
        # draws a new halftoned circle with size based on the diameter of the halftoning circle
        draw.ellipse((x, y, x + diameter, y + diameter), fill=255) 
# saves new halftoned image
halftoned.save("halftoned.jpg") 

# colorizes halftoned image in purple (wanted blue but since it's only one value...)
color = ImageFilter.colorize(halftoned, (0,0,255), (255,0,255))
# saves final image as a blend of halftoned and new colorized image (lightens)
final = Image.blend(halftoned, color, 0.5)
# saves final filtered image
final.save("filtered.jpg")