from PIL import Image, ImageDraw, ImageStat
import sys

def halftone(im, sample, scale):
    im = im.split() # splits image into RGB channels
    shades = [] # layer of pixels to be merged
    angle = 0
    channel=im[2]
    size = channel.size[0]*scale, channel.size[1]*scale
    half_tone = Image.new('L', size)
    draw = ImageDraw.Draw(half_tone)
    for x in range(0, channel.size[0], sample):
        for y in range(0, channel.size[1], sample):
            box = channel.crop((x, y, x + sample, y + sample))
            stat = ImageStat.Stat(box)
            diameter = (stat.mean[0] / 255)**0.5
            edge = 0.5*(1-diameter)
            x_pos, y_pos = (x+edge)*scale, (y+edge)*scale
            box_edge = sample*diameter*scale
            draw.ellipse((x_pos, y_pos, x_pos + box_edge, y_pos + box_edge), fill=255)
    for x in range(3):
    	shades.append(half_tone)
    return shades

image = Image.open(sys.argv[1])

shades = halftone(image, 30, 1)
new = Image.merge('RGB', shades)
new.save("filtered3.jpg")