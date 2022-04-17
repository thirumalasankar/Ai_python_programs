#water jug prob using bfs 
#water jug prob using dfs
class waterjug:
    def __init__(self,mbj,msj,goal):
        self.mbj=mbj
        self.msj=msj
        self.bj=0
        self.sj=0
        self.goal=goal
    def bfs(self):
        open=[]
        closed=[]
        open.append((self.bj,self.sj))
        print(open,end=" ")
        print(closed)
        while open:
            #for bfs
            #rec=open.pop(0)
            #for dfs
            rec=open.pop()
            if rec not in closed:
                closed.append(rec)
            #print(rec)
            bj=rec[0]
            sj=rec[1]
            # rules for filling water jug
            # water poured from bj to sj in this approach
            if sj==self.goal or bj==self.goal:
                print("successfull measured")
                print(closed)
                return 
            #fill big jug
            if bj==0 and ((self.mbj,sj) not in closed):
                open.append((self.mbj,sj))
            #fill small jug
            if sj==0 and ((bj,self.msj) not in closed):
                open.append((bj,self.msj))
            #empty big jug
            if bj==self.mbj and ((0,sj) not in closed):
                open.append((0,sj))
            #empty small jug
            if sj==self.msj and ((bj,0) not in closed):
                open.append((bj,0))
            if bj>0 and sj<self.msj:
                if bj>self.msj-sj:
                    t1=bj-(self.msj-sj)
                    t2=self.msj
                else:
                    t1=0
                    t2=sj+bj
                if (t1,t2) not in closed:
                    open.append((t1,t2))
            print(open,end=" ")
            print(closed)
bjs=int(input("enter size of big jug:"))
sjs=int(input("enter size of small jug:"))
goal=int(input("enter the goal measure:"))
obj=waterjug(bjs,sjs,goal)
obj.bfs()



"""
output:---


enter size of big jug:4
enter size of small jug:3
enter the goal measure:2
[(0, 0)] []
[(4, 0), (0, 3)] [(0, 0)]
[(4, 0), (4, 3)] [(0, 0), (0, 3)]
[(4, 0), (4, 0)] [(0, 0), (0, 3), (4, 3)]
[(4, 0), (1, 3)] [(0, 0), (0, 3), (4, 3), (4, 0)]
[(4, 0), (1, 0)] [(0, 0), (0, 3), (4, 3), (4, 0), (1, 3)]
[(4, 0), (0, 1)] [(0, 0), (0, 3), (4, 3), (4, 0), (1, 3), (1, 0)]
[(4, 0), (4, 1)] [(0, 0), (0, 3), (4, 3), (4, 0), (1, 3), (1, 0), (0, 1)]
[(4, 0), (2, 3)] [(0, 0), (0, 3), (4, 3), (4, 0), (1, 3), (1, 0), (0, 1), (4, 1)]
successfull measured
[(0, 0), (0, 3), (4, 3), (4, 0), (1, 3), (1, 0), (0, 1), (4, 1), (2, 3)]

"""
