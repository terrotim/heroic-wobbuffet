import random
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

overallMap=numpy.zeros((30,3))
redTotal=[]
blueTotal=[]
greenTotal=[]

# Location of the battle areas on the map
nodeLocations=[
    [790,1075],
    [1160,1105],
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

for iteration in range(0,10000):
    nodes = []
    
    #Battle 1
    edges = [
        [1,2],[1,4],
        [2,7],
        [3,8],[3,11],
        [4,5],[4,6],
        [5,8],[5,10],
        [6,9],
        [7,9],[7,13],
        [8,11],
        [9,16],
        [10,15],
        [11,12],
        [12,14],[12,17],
        [13,16],
        [14,15],
        [15,18],
        [16,20],[16,22],
        [17,19],[17,21],
        [18,21],[18,22],
        [19,26],
        [20,24],
        [21,23],
        [22,25],
        [23,26],[23,28],
        [24,25],[24,27],
        [26,29],
        [27,30],
        [28,29],[28,30]
        ]
    hqs = [3,13,29]
    startingRed = [2,6,7,9,13,16,20,22,24,25]
    startingBlue = [1,3,4,5,8,10,11,12,14,15]
    startingGreen = [17,18,19,21,23,26,27,28,29,30]
    
    
    """
    #Battle 2
    edges = [
        [1,3],[1,4],
        [2,6],[2,7],
        [3,8],
        [4,5],[4,6],
        [5,8],[5,10],
        [6,9],
        [7,9],[7,13],
        [8,11],
        [9,10],[9,16],
        [10,12],[10,15],
        [11,12],
        [12,14],[12,17],
        [13,16],
        [14,21],
        [15,16],
        [16,20],[16,22],
        [17,19],[17,21],
        [18,21],[18,22],[18,28],
        [19,23],[19,26],
        [20,24],
        [21,23],
        [22,25],
        [23,28],
        [24,25],[24,27],
        [26,29],
        [27,30],
        [28,29]
        ]
    hqs = [2,26,27]
    startingRed = [11,12,14,17,19,21,23,26,28,29]
    startingBlue = [1,2,3,4,5,6,7,8,9,10]
    startingGreen = [13,15,16,18,20,22,24,25,27,30]
    """
    
    """ 
    #Battle 3
    edges = [
        [1,2],[1,4],
        [2,6],[2,7],
        [3,5],[3,8],[3,11],
        [4,5],[4,6],
        [5,8],[5,10],
        [6,9],[6,10],
        [7,9],
        [8,12],
        [9,13],[9,16],
        [10,12],[10,14],[10,15],
        [11,12],
        [12,17],
        [13,16],[13,20],
        [14,15],[14,21],
        [15,16],[15,18],
        [16,20],[16,22],
        [17,19],[17,21],
        [18,21],[18,22],
        [19,23],
        [20,24],
        [21,23],
        [22,25],
        [23,25],[23,26],[23,28],
        [25,27],[25,28],
        [26,29],
        [27,30],
        [28,29],[28,30]
        ]
    hqs = [7,11,30]
    startingRed = [1,2,4,5,6,7,9,10,15,16]
    startingBlue = [13,18,20,22,24,25,27,28,29,30]
    startingGreen = [3,8,11,12,14,17,19,21,23,26]
    """
    
    colors = {0:'red',1:'blue',2:'green'}
    points = [1480,1220,960,740]


    # Initialize the nodes
    for x in startingRed:
        node = {
            "id":x,
            "soldiers":{
                "red":5000,
                "blue":0,
                "green":0
            },
            "color":colors[0]
        }
        nodes.append(node)

    for x in startingBlue:
        node = {
            "id":x,
            "soldiers":{
                "red":0,
                "blue":5000,
                "green":0
            },
            "color":colors[1]
        }
        nodes.append(node)

    for x in startingGreen:
        node = {
            "id":x,
            "soldiers":{
                "red":0,
                "blue":0,
                "green":5000
            },
            "color":colors[2]
        }
        nodes.append(node)

    for x in range(0,22):
        # Get nodes of combat for each color in current round from obtained edges.
        battlingRed = set()
        battlingBlue = set()
        battlingGreen = set()
        for edge in edges:
            node1 = next((x for x in nodes if x['id'] == edge[0]), None)
            node2 = next((x for x in nodes if x['id'] == edge[1]), None)
            # Add node to list of active battling nodes only if it is not an HQ.
            if node1["color"] != node2["color"]:
                if node1["color"] == 'red' or node2["color"] == "red":
                    if node1['id'] not in hqs:
                        battlingRed.add(node1['id'])
                    if node2['id'] not in hqs:
                        battlingRed.add(node2['id'])
                if node1["color"] == 'blue' or node2["color"] == "blue":
                    if node1['id'] not in hqs:
                        battlingBlue.add(node1['id'])
                    if node2['id'] not in hqs:
                        battlingBlue.add(node2['id'])
                if node1["color"] == 'green' or node2["color"] == "green":
                    if node1['id'] not in hqs:
                        battlingGreen.add(node1['id'])
                    if node2['id'] not in hqs:
                        battlingGreen.add(node2['id'])
    
        # Randomly assign 200 soldiers to nodes of combat of associated color

        #Assign reds
        for s in range(0,200):
            #Chance that the soldier actually plays
            if random.randint(1, 6)==6:
                target = random.sample(battlingRed,1)[0]
                targetNode = next((x for x in nodes if x['id'] == target),None)
                #How much stamina used in the battle
                score = random.choice(points)*random.randint(1, 8)
                targetNode["soldiers"]["red"] += score
                #Splash damage
                splashNodes=set()
                 #Find all edges that contain targetNode
                for edge in edges:
                    if targetNode["id"] in edge:
                        #Are both nodes in the edge a member of battlingRed?
                        #If so, add portion of score to the splash nodes
                        if edge[0] in battlingRed:
                            splashNodes.add(edge[0])
                        if edge[1] in battlingRed:
                            splashNodes.add(edge[1])
                splashNodes.remove(targetNode["id"])
                for node in splashNodes:
                    splashNode = next((x for x in nodes if x['id'] == node),None)
                    splashNode["soldiers"]["red"] += score/2
                
        #Assign blues
        for s in range(0,200):
            #Chance that the soldier actually plays
            if random.randint(1, 6)==6 :
                target = random.sample(battlingBlue,1)[0]
                targetNode = next((x for x in nodes if x['id'] == target),None)
                #How much stamina used in the battle
                score = random.choice(points)*random.randint(1, 8)
                targetNode["soldiers"]["blue"] += score
                #Splash damage
                splashNodes=set()
                for edge in edges:
                    if targetNode["id"] in edge:
                        if edge[0] in battlingBlue:
                            splashNodes.add(edge[0])
                        if edge[1] in battlingBlue:
                            splashNodes.add(edge[1])
                splashNodes.remove(targetNode["id"])
                for node in splashNodes:
                    splashNode = next((x for x in nodes if x['id'] == node),None)
                    splashNode["soldiers"]["blue"] += score/2

        #Assign greens
        for s in range(0,200):
            #Chance that the soldier actually plays
            if random.randint(1, 6)==6 :
                target = random.sample(battlingGreen,1)[0]
                targetNode = next((x for x in nodes if x['id'] == target),None)
                #How much stamina used in the battle
                score = random.choice(points)*random.randint(1, 8)
                targetNode["soldiers"]["green"] += score
                #Splash damage
                splashNodes=set()
                for edge in edges:
                    if targetNode["id"] in edge:
                        if edge[0] in battlingGreen:
                            splashNodes.add(edge[0])
                        if edge[1] in battlingGreen:
                            splashNodes.add(edge[1])
                splashNodes.remove(targetNode["id"])
                for node in splashNodes:
                    splashNode = next((x for x in nodes if x['id'] == node),None)
                    splashNode["soldiers"]["green"] += score/2

                    
        # End of round. Assess scenario and change node colors accordingly
        for node in nodes:
            node['color']=(max(node['soldiers'], key=node['soldiers'].get))
            #Reset nodes to appropriate starting score
            if node['color']=='red':
                node['soldiers']={"red":5000,"blue":0,"green":0}
            elif node['color']=='blue':
                node['soldiers']={"red":0,"blue":5000,"green":0}
            else:
                node['soldiers']={"red":0,"blue":0,"green":5000}
        # Repeat for 22 rounds.

    
    numRed=0
    numBlue=0
    numGreen=0
    for node in nodes:
        if node['color']=='red':
            numRed += 1
            overallMap[node['id']-1][0] +=1
        elif node['color']=='blue':
            numBlue += 1
            overallMap[node['id']-1][1] +=1
        else:
            numGreen += 1
            overallMap[node['id']-1][2] +=1

    redTotal.append(numRed)
    blueTotal.append(numBlue)
    greenTotal.append(numGreen)
    print(iteration, numRed, numBlue,numGreen)
    # print(overallMap)
    # Repeat for 10000 battles
    
print(sum(redTotal)/len(redTotal))
print(sum(blueTotal)/len(blueTotal))
print(sum(greenTotal)/len(greenTotal))
#print(overallMap)

#labels = 'Alfonse', 'Sharena', 'Anna'
colors = ['red', 'deepskyblue', 'green']
areaNum = 1

#Save pies as images
for areas in overallMap:
    fig1, ax1 = plt.subplots()
    ax1.pie(areas,colors=colors,startangle=90)
    ax1.axis('equal')
    plt.suptitle(areaNum, fontsize=36)
    plt.tight_layout()
    plt.savefig('area_'+str(areaNum)+'.png')
    areaNum += 1
    plt.cla()
    plt.close(fig1)

#Pastes the pie charts onto the map image, usually a screenshot of the map.
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