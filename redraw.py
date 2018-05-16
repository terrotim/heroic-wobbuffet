import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# Redraws final_map based on generated images from GC_Simulation.py, mostly to readjust the nodeLocations values.
nodeLocations=[
    [790,1075],
    [1170,1105],
    [200,1140],
    [730,1210],
    [545,1290],
    [835,1345],
    [1155,1360],
    [360,1375],
    [940,1480],
    [660,1500],
    [125,1505],
    [410,1585],
    [1185,1545],
    [570,1690],
    [740,1705],
    [965,1725],
    [340,1800],
    [720,1840],
    [115,1855],
    [1185,1860],
    [545,1875],
    [840,1965],
    [360,2020],
    [1135,2040],
    [890,2110],
    [110,2125],
    [1105,2225],
    [480,2250],
    [265,2275],
    [895,2305]
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