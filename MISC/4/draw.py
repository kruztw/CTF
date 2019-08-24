from PIL import Image
from math import sqrt

file = open("data.txt","r").read()

width = int(sqrt(len(file)))

pixels = [(0,0,0) if i == '1' else (255,255,255) for i in file]

im = Image.new("RGB",(width,width))
im.putdata(pixels)
im.save("QR.png")