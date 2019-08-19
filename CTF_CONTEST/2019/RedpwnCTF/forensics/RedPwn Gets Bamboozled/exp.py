from PIL import Image

with open('data.txt', 'r') as file:
    data = file.read()

width = 600
height = 800
data = data[8:len(data)].split(', ')

for i in range(0,len(data)):
    data[i] = data[i][1:len(data[i])-1].split(' ')

im = Image.new('RGB',(width, height))
for j in range(0,height):
    for i in range(0,width):
        im.putpixel((i,j), (int(data[j*width + i][0]), int(data[j*width + i][1]), int(data[j*width + i][2])))
im.save("output.png")