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
        #s=openList.pop(0)
        #for DFS---
        s=openList.pop(len(openList)-1)
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
    
    
"""
output:--


A
J
['A'] []
['B', 'C', 'D'] ['A']
['B', 'C'] ['A', 'D']
['B', 'F', 'G'] ['A', 'D', 'C']
['B', 'F'] ['A', 'D', 'C', 'G']
['B', 'J'] ['A', 'D', 'C', 'G', 'F']
['B'] ['A', 'D', 'C', 'G', 'F', 'J']
the goalstate: J is found

"""
