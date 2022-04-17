#bfs with open list(queue) and closed list(stack)
#dfs with open list and closed list
graph={'A':['B','C','D'],'B':['E','F'],'C':['F','G'],'D':[],'E':['H','I'],'F':['J'],'G':[],'H':[],'I':[],'J':[]}
startNode=input()
goalNode=input()
openList=[]
closedList=[]
found=False
def bfs(node):
    if node not in openList:
        openList.append(node)
    print(openList,end=' ')
    print(closedList)
    while len(openList)!=0:
        #for BFS---
        s=openList.pop(0)
        #for DFS---
        #s=openList.pop(len(openList)-1)
        if s not in closedList:
            closedList.append(s)
        for neighbour in graph[s]:
            if neighbour not in closedList:
                openList.append(neighbour)
        print(openList,end=' ')
        print(closedList)
        if s==goalNode:
            found=True
            return found  
goalFound=bfs(startNode)
if goalFound:
    print(f"the goalstate: {goalNode} is found")
else:
    print(f"the goalstate: {goalNode} is not found")

    
    
"""output:--


A
J
['A'] []
['B', 'C', 'D'] ['A']
['C', 'D', 'E', 'F'] ['A', 'B']
['D', 'E', 'F', 'F', 'G'] ['A', 'B', 'C']
['E', 'F', 'F', 'G'] ['A', 'B', 'C', 'D']
['F', 'F', 'G', 'H', 'I'] ['A', 'B', 'C', 'D', 'E']
['F', 'G', 'H', 'I', 'J'] ['A', 'B', 'C', 'D', 'E', 'F']
['G', 'H', 'I', 'J', 'J'] ['A', 'B', 'C', 'D', 'E', 'F']
['H', 'I', 'J', 'J'] ['A', 'B', 'C', 'D', 'E', 'F', 'G']
['I', 'J', 'J'] ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
['J', 'J'] ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
['J'] ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
the goalstate: J is found

"""

