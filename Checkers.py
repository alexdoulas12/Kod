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
def move_pawn(lista):
    while True:
        p=input("Välj en bricka att flytta ").upper()
        y=int((ord(p[0])-65))
        x=int(p[1])

        if(len(lista) > 0):
            if([x, y] not in lista):
                print("The following pawns have moves:")
                for pawn in lista:
                    print(chr(pawn[1] + 65) + str(pawn[0]))
                continue
        if b[x][y]!=None and b[x][y].color=="B":
            while True:#Flyttar svart spelare
                k=input("Välj en bricka att flytta till ").upper()
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
                k=input("Välj en bricka att flytta till ").upper()
                w=int((ord(k[0])-65))
                z=int(k[1])
                if z==x-1 and (w==y+1 or w==y-1):
                    if b[z][w]==None: 
                        b[z][w]=b[x][y]
                        b[x][y]=None
                        return False

def check(c):
    lista=[]
    print("CHECK")
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if b[y][x] != None and b[y][x].color == c:
                if(is_valid_move(y, x)):
                    lista.append([y, x])
    print(lista)
    return  lista

def is_valid_move(y, x):    
    pawn = b[y][x]
    #   If the pawn is white
    if(pawn.color == "W"):
        if(can_jump_up(y)):
            if(can_jump_left(x)):

                #   Checks if there is a black pawn top left
                if(b[y - 1][x - 1] != None and b[y - 1][x - 1].color == "B"):
                    if(b[y - 2][x - 2] == None):
                        return True

            if(can_jump_right(x)):

                #   Checks if there is a black pawn top right
                if(b[y - 1][x + 1] != None and b[y - 1][x + 1].color == "B"):
                    if(b[y - 2][x + 2] == None):
                        return True

    return False

def can_jump_up(y):
    if(y - 2 >= 0):
        return True
    else:
        return False

def can_jump_left(x):
    if(x - 2 >= 0):
        return True
    else:
        return False

def can_jump_right(x):
    if(x + 2 < GRID_SIZE):
        return True
    else:
        return False

def main():
    
    while(True):
        #   White move
        print_board(b)
        lista=check("W")
        print("White's turn")
        move_pawn(lista)

        #   Black move
        print_board(b)
        print("Black's turn")
        lista=check("B")
        move_pawn(lista)


main()

