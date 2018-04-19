import random

redTotal=[]
blueTotal=[]
greenTotal=[]
for iteration in range(0,10000):
    nodes = []
    
    #Battle 1
    edges = [
        [1,3],[1,4],[1,7],
        [2,3],[2,9],
        [3,6],
        [4,8],
        [5,7],[5,11],
        [6,8],[6,9],
        [7,10],[7,12],
        [8,13],[8,14],
        [9,15],
        [10,11],[10,12],
        [11,17],
        [12,13],[12,16],
        [13,18],
        [14,15],
        [15,19],
        [16,17],[16,20],
        [18,19],[18,21],
        [19,21],
        [20,21],[20,22],
        [21,26],
        [22,24],[22,25],
        [23,24],[23,27],
        [25,29],[25,30],
        [26,28],
        [27,29],
        [28,30]
        ]
    hqs = [2,17,28]
    startingRed = [1,2,3,4,6,8,9,13,14,15]
    startingBlue = [18,19,21,23,25,26,27,28,29,30]
    startingGreen = [5,7,10,11,12,16,17,20,22,24]
    
    
    """
    #Battle 2
    edges = [
        [1,4],[1,5],
        [2,3],[2,9],
        [3,4],[3,6],
        [4,8],
        [5,7],[5,11],
        [6,9],
        [7,8],[7,10],[7,13],
        [8,9],[8,14],
        [10,11],[10,12],[10,16],
        [12,13],
        [13,18],[13,20],
        [14,15],[14,18],
        [15,19],
        [16,17],[16,20],
        [17,23],
        [18,19],[18,20],[18,21],
        [19,26],
        [20,22],
        [21,22],[21,25],[21,26],
        [22,24],
        [23,24],[23,27],
        [24,29],
        [25,29],[25,30],
        [26,28],
        [27,29],
        [28,30],
        ]
    hqs = [1,15,27]
    startingRed = [1,2,3,4,5,7,10,11,12,16]
    startingBlue = [6,8,9,13,14,15,18,19,21,26]
    startingGreen = [17,20,22,23,24,25,27,28,29,30]
    """
    
    """
    #Battle 3
    edges = [
        [1,4],[1,5],[1,7],
        [2,3],[2,6],
        [3,4],[3,6],
        [4,8],[4,12],
        [5,11],
        [6,8],[6,9],
        [7,10],[7,12],
        [8,13],[8,14],
        [9,15],
        [10,11],[10,12],
        [11,17],
        [12,13],[12,16],
        [13,18],
        [14,15],[14,18],
        [16,17],[16,18],[16,20],
        [17,22],
        [18,19],[18,20],[18,21],
        [19,26],
        [20,22],
        [21,25],[21,26],[21,28],
        [22,24],[22,25],
        [23,24],[23,27],
        [24,29],
        [25,29],[25,29],
        [26,28],
        [27,29],
        [28,30],
        ]
    hqs = [5,15,27]
    startingRed = [6,8,9,13,14,15,18,19,21,26]
    startingBlue = [16,20,22,23,24,25,27,28,29,30]
    startingGreen = [1,2,3,4,5,7,10,11,12,17]
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
            if random.randint(1, 8)==8:
                target = random.sample(battlingRed,1)[0]
                targetNode = next((x for x in nodes if x['id'] == target),None)
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
            if random.randint(1, 8)==8 :
                target = random.sample(battlingBlue,1)[0]
                targetNode = next((x for x in nodes if x['id'] == target),None)
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
            if random.randint(1, 8)==8 :
                target = random.sample(battlingGreen,1)[0]
                targetNode = next((x for x in nodes if x['id'] == target),None)
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
        elif node['color']=='blue':
            numBlue += 1
        else:
            numGreen += 1

    redTotal.append(numRed)
    blueTotal.append(numBlue)
    greenTotal.append(numGreen)
    print(iteration, numRed, numBlue,numGreen)
    # Repeat for 10000 battles
    
print(sum(redTotal)/len(redTotal))
print(sum(blueTotal)/len(blueTotal))
print(sum(greenTotal)/len(greenTotal))