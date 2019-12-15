import datetime
start = datetime.datetime.now().time
print(start)
#end=datetime.datetime.now().time
#return 
class Pawn(object):

    def __init__(self,color,isdam):
            self.color=color
            self.isdam=isdam
GRID_SIZE = 8
def create_board():
    board=[]
    for i in range(GRID_SIZE):
        r = []
        for j in range(GRID_SIZE):
            r.append(None)
            if i<(GRID_SIZE/2)-1 and i%2==0:
                if j<GRID_SIZE and j%2 !=0:
                    r[j]=Pawn("B",False)
                    
                   #r.append(pos(Black,False))
            if i<(GRID_SIZE/2)-1 and i%2 !=0:
                if j<GRID_SIZE and j%2 ==0:
                    r[j]=Pawn("B",False)
                    
                    #r.append(pos(Black,False))
            if i>GRID_SIZE/2 and i%2==0:
                if j<GRID_SIZE and j%2 !=0:
                    r[j]=Pawn("W",False)
                    #r.append(pos(White,False))
            if i>GRID_SIZE/2 and i%2 !=0:
                if j<GRID_SIZE and j%2 ==0:
                    r[j]=Pawn("W",False)
                    #r.append(pos(White,False))
        board.append(r)
    return board
def print_board(board):
    print("     ", end="")
    for i in range(GRID_SIZE):
        j=chr(i+65)
        print(j, end=" ")
    print("")
    print("")
    for rad in board:
        i+=1
        print(i-GRID_SIZE, end="    ")
        for pos in rad:
            if pos is None:
                print("-", end=" ")
            else:
                print(pos.color, end=" ")
        print("")
    print("")
b = create_board()
#vit standardrörelse fram index:[-1][+-1]
#svart standardrörelse fram index:[+1][+-1]
#vit capture index:[-2][+-2]
#svart capture index:[+2][+-2]
def move_pawn():
    while True:
        p=input("Välj en bricka att flytta ")
        y=int((ord(p[0])-65))
        x=int(p[1])
        if b[x][y]!=None and b[x][y].color=="B":
            while True:#Flyttar svart spelare
                k=input("Välj en bricka att flytta till ")
                w=int((ord(k[0])-65))
                z=int(k[1])
                if z==x+1 and (w==y+1 or w==y-1):
                    if b[z][w]==None:
                        b[z][w]=b[x][y]
                        b[x][y]=None
                        return False
                    if b[z][w].color=="W":
                        if b[z+1][w+1]==None:
                            b[z+1][w+1]=b[x][y]
                            b[x][y]=None
                            return False
                    
        if b[x][y]!=None and b[x][y].color=="W":
            while True:#Flyttar svart spelare
                k=input("Välj en bricka att flytta till ")
                w=int((ord(k[0])-65))
                z=int(k[1])
                if z==x-1 and (w==y+1 or w==y-1):
                    if b[z][w]==None: 
                        b[z][w]=b[x][y]
                        b[x][y]=None
                        return False




def check():
    lista=[]
    print("CHECK")
    for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if b[x][y]!=None:
                    if b[x][y].color=="B":
                        print(b[x][y].color, (x,y))
                        if x==0:
                            if  b[x+1][x+1]!=None:
                                if  b[x+1][y+1].color=="W":
                                    if b[x+2][y+2]==None:
                                        print("dfghlkdfg")
                                        lista.append([x,y])
                                    
                        if x==GRID_SIZE-1:
                            if b[x+1][y-1]!=None:
                                if b[x+1][y-1].color=="W":
                                    if b[j+2][j-2]==None:
                                        print("JHABSFKBASF")
                                        lista.append([x,y])
                        if x==1:
                            if  b[x+1][y+1]!=None:
                                if  b[x+1][y+1].color=="W":
                                    if b[x+2][y+2]==None:
                                        print("dfghlkdfg")
                                        lista.append([x,y])

                        if x==GRID_SIZE-1:
                            if b[x+1][y-1]!=None:
                                if b[x+1][y-1].color=="W":
                                    if b[x+2][y-2]==None:
                                        print("JHABSFKBASF")
                                        lista.append([x,y])

                        if x>1 and x<GRID_SIZE-2:
                            if  b[x+1][y+1]!=None or b[x+1][y-1]!=None:
                                if  b[j+1][i+1].color=="W" or b[j+1][i-1].color=="W":
                                    print("HAHA")
                                    if b[x+2][y+2]==None or b[x+2][y-2]==None:
                                        print("ajajaj")
                                        lista.append([x,y])

    return  lista
                                                  
                            
def main():
    for m in range(3):
        print_board(b)
        lista=check()
        move_pawn()
        print(lista)

main()
#print(lista)

