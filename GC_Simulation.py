import random
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

overallMap=numpy.zeros((30,3))
redTotal=[]
blueTotal=[]
greenTotal=[]

def getStartingScore(numNodes):
    if numNodes <= 2:
        return 15000
    elif 3 <= numNodes <= 4:
        return 12500
    elif 5 <= numNodes <= 6:
        return 10000
    elif 7 <= numNodes <= 8:
        return 7500
    else:
        return 5000

# Location of the battle areas on the map
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

for iteration in range(0,10000):
    nodes = []
    
    #Battle 1
    edges = [
        [1,2],[1,3],
        [2,6],
        [3,4],[3,7],
        [4,8],
        [5,9],
        [6,10],
        [7,8],[7,11],
        [8,13],
        [9,10],[9,12],
        [10,16],
        [11,12],[11,15],
        [12,14],
        [13,17],
        [14,18],[14,20],
        [15,17],[15,19],
        [16,18],
        [17,21],
        [18,23],
        [19,20],[19,25],
        [20,24],
        [21,27],
        [22,23],[22,26],
        [23,24],
        [24,28],
        [25,27],[25,29],
        [26,30],
        [28,29],[28,30],
        ]
    hqs = [6,13,30]
    startingRed = [1,2,5,6,9,10,12,14,16,18]
    startingBlue = [19,20,22,23,24,25,26,28,29,30]
    startingGreen = [3,4,7,8,11,13,15,17,21,27]
    
    """
    #Battle 2
    edges = [
        [1,6],[1,7],
        [2,3],[2,5],
        [3,8],
        [4,5],[4,6],
        [5,9],
        [6,11],
        [7,10],
        [8,13],[8,16],
        [9,12],[9,13],
        [10,11],[10,15],
        [11,12],[11,14],
        [13,16],
        [14,15],[14,17],
        [15,18],
        [16,20],[16,21],
        [17,19],[17,20],
        [18,22],
        [19,22],[19,24],
        [20,23],[20,25],
        [21,26],
        [22,28],
        [23,27],[23,29],
        [24,27],
        [25,26],
        [26,30],
        [27,28],
        [29,30],
        ]
    hqs = [1,21,28]
    startingRed = [3,8,13,16,20,21,25,26,29,30]
    startingBlue = [1,2,4,5,6,7,9,10,11,12]
    startingGreen = [14,15,17,18,19,22,23,24,27,28]
    """
    """
    #Battle 3
    edges = [
        [1,6],[1,7],
        [2,3],[2,4],
        [3,8],
        [4,5],[4,6],
        [5,9],
        [6,11],
        [7,10],
        [8,9],[8,16],
        [9,12],
        [10,11],[10,15],
        [11,14],
        [12,13],[12,17],[12,20],
        [13,21],
        [14,15],[14,17],
        [15,18],
        [16,21],
        [17,19],[17,20],
        [18,19],[18,22],
        [20,23],[20,25],
        [21,26],
        [22,24],[22,28],
        [23,24],[23,29],
        [25,26],
        [26,30],
        [27,28],[27,29],
        [29,30],
        ]
    hqs = [3,7,27]
    startingRed = [2,3,4,5,8,9,12,13,16,21]
    startingBlue = [1,6,7,10,11,14,15,17,18,19]
    startingGreen = [20,22,23,24,25,26,27,28,29,30]
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
            if random.randint(1, 8)==8:
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
            if random.randint(1, 8)==8 :
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
            if random.randint(1, 8)==8 :
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

        numRed=0
        numBlue=0
        numGreen=0     
        # End of round. Assess scenario and change node colors accordingly
        for node in nodes:
            node['color']=(max(node['soldiers'], key=node['soldiers'].get))
            #Reset nodes to appropriate starting score
            if node['color']=='red':
                numRed += 1
            elif node['color']=='blue':
                numBlue += 1
            else:
                numGreen += 1
                
        #TODO dynamic starting score depending on how many nodes a team has left
        

        redStartingScore = getStartingScore(numRed)
        blueStartingScore = getStartingScore(numBlue)
        greenStartingScore = getStartingScore(numGreen)
        
        for node in nodes:
            #Reset nodes to appropriate starting score
            if node['color']=='red':
                node['soldiers']={"red":redStartingScore,"blue":0,"green":0}
            elif node['color']=='blue':
                node['soldiers']={"red":0,"blue":blueStartingScore,"green":0}
            else:
                node['soldiers']={"red":0,"blue":0,"green":greenStartingScore}
        
        
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
    plt.suptitle(areaNum, fontsize=72)
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