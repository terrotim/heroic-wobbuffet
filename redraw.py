import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# Redraws final_map based on generated images from GC_Simulation.py, mostly to readjust the nodeLocations values.
nodeLocations=[
    [600,1060],
    [990,1075],
    [340,1110],
    [100,1190],
    [810,1205],
    [1200,1250],
    [460,1330],
    [200,1360],
    [920,1375],
    [1130,1490],
    [470,1570],
    [815,1580],
    [160,1625],
    [755,1760],
    [505,1770],
    [1160,1780],
    [160,1780],
    [940,1830],
    [410,1925],
    [705,1960],
    [170,2005],
    [1170,2030],
    [920,2070],
    [590,2140],
    [310,2150],
    [1170,2240],
    [80,2260],
    [640,2310],
    [370,2315],
    [950,2315]
    ]

map = Image.open('map.png')

for locationNum in range(len(nodeLocations)):
    pie = Image.open('area_'+str(locationNum+1)+'.png')
    pie = pie.resize((160,120))
    data = pie.getdata()
    newData = []
    for pixel in data:
        if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(pixel)
    pie.putdata(newData)
    map.paste(pie,nodeLocations[locationNum],pie)
    pie.close()

map.show()
map.save("final_map.png", "PNG")
map.close()