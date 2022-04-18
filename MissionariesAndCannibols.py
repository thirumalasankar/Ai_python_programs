#machinaries and cannibals using bfs
#machinaries and cannibals using dfs
class mandc:
    def __init__(self,m,c,startState,goalState):
        self.m=m
        self.c=c
        self.startState=startState
        self.goalState=goalState
    def bfs(self):
        open=[self.startState]
        closed=[]
        """print("open")                
        print(open,end=" ")
        print()
        print("closed")
        print(closed)"""
        print("([M, C, B], [M, C, B])")
        while open:
            #for bfs 
            p=open.pop(0)
            #for dfs
            #p=open.pop()
            l=p[0]
            r=p[1]
            lm=l[0]
            lc=l[1]
            lb=l[2]
            rm=r[0]
            rc=r[1]
            rb=r[2]
            if p not in closed:
                closed.append(p)
                print(p)
            if p==self.goalState:
                print("Goal is found through BFS")
                break
            #left to right rules boat moving rules
            if lb==1:
                if lm-2 >=0 and rm+2>=rc and rm+2<=3:
                    if lm-2==0 or lm-2>=lc:
                        if ([lm-2,lc,0],[rm+2,rc,1]) not in closed:
                            open.append(([lm-2,lc,0],[rm+2,rc,1]))
                if lm-1>=0 and lc-1>=0 and rm+1<=3 and rc+1<=3 and rm+1>=rc+1 :
                    if ([lm-1,lc-1,0],[rm+1,rc+1,1]) not in closed:
                        open.append(([lm-1,lc-1,0],[rm+1,rc+1,1]))
                if lc-2>=0 and rc+2<=3:
                    if rm==0 or rc+2<=rm :
                        if ([lm,lc-2,0],[rm,rc+2,1]) not in closed:
                            open.append(([lm,lc-2,0],[rm,rc+2,1]))
                if lm-1>=0 and rm+1>=rc and rm+1<=3:
                    if lm-1==0 or lm-1>=lc:
                        if ([lm-1,lc,0],[rm+1,rc,1]) not in closed:
                            open.append(([lm-1,lc,0],[rm+1,rc,1]))
                if lc-1>=0 and rc+1<=3:
                    if rm==0 or rc+1<=rm:
                        if ([lm,lc-1,0],[rm,rc+1,1]) not in closed:
                            open.append(([lm,lc-1,0],[rm,rc+1,1]))
            else:
              #right to left boat moving rules
                if rm-2>=0 and lm+2<=3 and lm+2>=lc:
                    if rm-2==0 or rm-2>=rc:
                        if ([lm+2,lc,1],[rm-2,rc,0]) not in closed:
                            open.append(([lm+2,lc,1],[rm-2,rc,0]))
                if rm-1>=0 and rc-1>=0 and lc+1<=3 and lm+1<=3 and lm+1>=lc+1:
                    if ([lm+1,lc+1,1],[rm-1,rc-1,0]) not in closed:
                        open.append(([lm+1,lc+1,1],[rm-1,rc-1,0]))
                if rc-2>=0 and lc+2<=3:
                    if lm==0 or lc+2<=lm: 
                        if ([lm,lc+2,1],[rm,rc-2,0]) not in closed:
                            open.append(([lm,lc+2,1],[rm,rc-2,0]))
                if rm-1>=0 and lm+1>=lc and lm+1<=3:
                    if rm-1==0 or rm-1>=rc:
                        if ([lm+1,lc,1],[rm-1,rc,0]) not in closed:
                            open.append(([lm+1,lc,1],[rm-1,rc,0]))
                if rc-1>=0 and lc+1<=3 :
                    if lm==0 or lc+1<=lm:
                        if ([lm,lc+1,1],[rm,rc-1,0]) not in closed:
                            open.append(([lm,lc+1,1],[rm,rc-1,0]))
            """print("open")                
            print(open,end=" ")
            print()
            print("closed")
            print(closed)"""
startState=([3,3,1],[0,0,0])
goalState=([0,0,0],[3,3,1])
obj=mandc(3,3,startState,goalState)  
obj.bfs()



"""
output:--


([M, C, B], [M, C, B])
([3, 3, 1], [0, 0, 0])
([2, 2, 0], [1, 1, 1])
([3, 1, 0], [0, 2, 1])
([3, 2, 0], [0, 1, 1])
([3, 2, 1], [0, 1, 0])
([3, 0, 0], [0, 3, 1])
([3, 1, 1], [0, 2, 0])
([1, 1, 0], [2, 2, 1])
([2, 2, 1], [1, 1, 0])
([0, 2, 0], [3, 1, 1])
([0, 3, 1], [3, 0, 0])
([0, 1, 0], [3, 2, 1])
([1, 1, 1], [2, 2, 0])
([0, 2, 1], [3, 1, 0])
([0, 0, 0], [3, 3, 1])
Goal is found through BFS


"""
