from pdb import set_trace
import datetime
start = datetime.datetime.now().time
#print(start)
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
#!!!TILL NÄSTA GÅNG!!!
# 1.) Tidsfunktion + highscore-lista

def valid_move_from():
    while True:
            try:
                p=input("Choose a pawn to move ").upper()
                y=int(p[1])
                if p[0]==quit:
                    print("Shutting down")
                    global Game_running
                    Game_running=True
                    return
                elif y>GRID_SIZE-1 or y<0:
                    print("Choose a pawn in the form of: A5 B2 C9...")
                    continue
                elif len(p)>2:
                    print("Choose a pawn in the form of: A5 B2 C9...")
                    continue
                else:
                    return p
            except IndexError:
                print("IndexError")
                continue
            except ValueError:
                print(p)
                print("ValueError")
                continue

def valid_move_to():
    while True:
            try:
                k=input("Choose a pawn to move to ").upper()

                z=int(k[1])
                if k[0]==quit:
                    print("Shutting down")
                    global Game_running
                    Game_running=True
                    return
                elif z>GRID_SIZE-1 or z<0:
                    print("Choose a pawn in the form of: A5 B2 C9...")
                    continue
                elif len(k)>2:
                    print("Choose a pawn in the form of: A5 B2 C9...")
                    continue
                else:
                    return k
            except IndexError:
                print("IndexError")
                continue
            except ValueError:
                print("ValueError")
                continue

def move_pawn(lista,c):
    move_made=False
    Outer=True
    while Outer:
        p=valid_move_from()
        
        x=int((ord(p[0])-65))
        y=int(p[1])
        if(len(lista) > 0):
            if([y, x] not in lista):
                print("The following pawns have moves:")
                for pawn in lista:
                    print(chr(pawn[1] + 65) + str(pawn[0]))
                continue
        if b[y][x]!=None and b[y][x].color!=c:
            continue
        
        if b[y][x]!=None and c=="B":
            if (len(lista)==0) and (b[y+1][x-1] and b[y+1][x+1])!=None:
                continue
            while True:#Flyttar svart spelare
                k=valid_move_to()
                w=int((ord(k[0])-65))
                z=int(k[1])
                if([y, x]) in lista:
                    if b[y][x].isdam==True:
                        if z==y-2:
                            if w==x-2:
                                b[z][w]=b[y][x]
                                b[z+1][w+1]=None
                                b[y][x]=None
                                Outer=False
                                move_made=True
                                check_for_queen(c, z, w)
                                break
                            if w==x+2:
                                b[z][w]=b[y][x]
                                b[z+1][w-1]=None
                                b[y][x]=None
                                Outer=False
                                move_made=True
                                check_for_queen(c, z, w)
                                break
                            else:
                                continue
                        else:
                            continue     
                    if z==y+2:
                        if w==x+2:
                            b[z][w]=b[y][x]
                            b[z-1][w-1]=None
                            b[y][x]=None
                            Outer=False
                            move_made=True
                            check_for_queen(c,z,w)
                            break
                            
                        if w==x-2:
                            b[z][w]=b[y][x]
                            b[z-1][w+1]=None
                            b[y][x]=None
                            Outer=False
                            move_made=True
                            check_for_queen(c, z, w)
                            break
                        else:
                            return True
                else:
                    if b[y][x].isdam==True:
                        if z==y-1 and (w==x+1 or w==x-1):
                            if b[z][w]==None: 
                                b[z][w]=b[y][x]
                                b[y][x]=None
                                Outer=False
                                check_for_queen(c, z, w)
                                break           
                    if z==y+1 and (w==x+1 or w==x-1):
                        if b[z][w]==None:
                            b[z][w]=b[y][x]
                            b[y][x]=None
                            Outer=False
                            check_for_queen(c, z, w)
                            break
                    
        if b[y][x]!=None and c=="W":
            if (len(lista)==0) and (b[y-1][x-1] and b[y-1][x+1])!=None:
                continue
            while True:#Flyttar vit spelare
                k=input("Välj en bricka att flytta till ").upper()
                w=int((ord(k[0])-65))
                z=int(k[1])
                if([y,x]) in lista:
                    if b[y][x].isdam==True:
                        if z==y+2:
                            if w==x+2:
                                b[z][w]=b[y][x]
                                b[z-1][w-1]=None
                                b[y][x]=None
                                Outer=False
                                move_made=True
                                check_for_queen(c,z,w)
                                break
                                
                            if w==x-2:
                                b[z][w]=b[y][x]
                                b[z-1][w+1]=None
                                b[y][x]=None
                                Outer=False
                                move_made=True
                                check_for_queen(c, z, w)
                                break
                            else:
                                continue
                    if z==y-2:
                        if w==x-2:
                            b[z][w]=b[y][x]
                            b[z+1][w+1]=None
                            b[y][x]=None
                            Outer=False
                            move_made=True
                            check_for_queen(c, z, w)
                            break
                        if w==x+2:
                            b[z][w]=b[y][x]
                            b[z+1][w-1]=None
                            b[y][x]=None
                            Outer=False
                            move_made=True
                            check_for_queen(c, z, w)
                            break
                        else:
                            continue
                    else:
                        continue
                else:
                    if b[y][x].isdam==True:
                        if z==y+1 and (w==x+1 or w==x-1):
                            if b[z][w]==None:
                                b[z][w]=b[y][x]
                                b[y][x]=None
                                Outer=False
                                check_for_queen(c, z, w)
                                break
                    if z==y-1 and (w==x+1 or w==x-1):
                        if b[z][w]==None: 
                            b[z][w]=b[y][x]
                            b[y][x]=None
                            Outer=False
                            check_for_queen(c, z, w)
                            break              
    else:
        if move_made:
            # lista=check(c)
            # for pawn in lista:
            #         print(chr(pawn[1] + 65) + str(pawn[0]))
            while (check_for_more_moves(c,lista,y,x,w,z)==True):   
                    another_move(c,lista)

def another_move(c,lista):
    for pawn in lista:
            x=pawn[1]
            y=pawn[0]
            print(chr(pawn[1] + 65) + str(pawn[0]))

    if c=="B":
        while True:#Flyttar svart spelare
            k=valid_move_to()
            w=int((ord(k[0])-65))
            z=int(k[1])
            if b[y][x].isdam==True:
                if z==y-2:
                    if w==x-2:
                        b[z][w]=b[y][x]
                        b[z+1][w+1]=None
                        b[y][x]=None
                        check_for_queen(c, z, w)
                        return False
                    if w==x+2:
                        b[z][w]=b[y][x]
                        b[z+1][w-1]=None
                        b[y][x]=None
                        check_for_queen(c, z, w)
                        return False
                else:
                    return True
            if z==y+2:
                if w==x+2:
                    b[z][w]=b[y][x]
                    b[z-1][w-1]=None
                    b[y][x]=None
                    check_for_queen(c, z, w)
                    return False
                elif w==x-2:
                    b[z][w]=b[y][x]
                    b[z-1][w+1]=None
                    b[y][x]=None
                    check_for_queen(c, z, w)
                    return False
                else:
                    return True
                
    if c=="W":
        while True:#Flyttar vit spelare
            k=input("Välj en bricka att flytta till ").upper()
            w=int((ord(k[0])-65))
            z=int(k[1])
            if b[y][x].isdam==True:
                if z==y+2:
                    if w==x+2:
                        b[z][w]=b[y][x]
                        b[z-1][w-1]=None
                        b[y][x]=None
                        check_for_queen(c, z, w)
                        return False
                    if w==x-2:
                        b[z][w]=b[y][x]
                        b[z-1][w+1]=None
                        b[y][x]=None
                        check_for_queen(c, z, w)
                        return False
                    else:
                        return True
            if z==y-2:
                if w==x-2:
                    b[z][w]=b[y][x]
                    b[z+1][w+1]=None
                    b[y][x]=None
                    check_for_queen(c, z, w)
                    return False
                if w==x+2:
                    b[z][w]=b[y][x]
                    b[z+1][w-1]=None
                    b[y][x]=None
                    check_for_queen(c, z, w)
                    return False
            else:
                return True

def check(c):
    lista=[]
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if b[y][x] != None and b[y][x].color ==c:
                if(is_valid_move(c, y, x)):
                    lista.append([y, x])
    return  lista

def check_for_queen(c, z, w):
    if c=="B" and z==GRID_SIZE-1:
        if b[z][w].isdam==False:
            print("The following piece has become a queen ", end="")
            print(chr(w+65)+str(z))
        b[z][w].isdam=True
    if c=="W" and z==0:
        if b[z][w].isdam==False:
            print("The following piece has become a queen ", end="")
            print(chr(w+65)+str(z))
        b[z][w].isdam=True

def check_for_more_moves(c,lista,x,y,w,z):
    lista=check(c)
    if len(lista)>0:
        if ([z, w]) in lista:
            print_board(b)
            for pawn in lista:
                print("Moving ", end="")
                print(chr(pawn[1] + 65) + str(pawn[0]))
            return True
        else:
            return False
    else:
        return False
    return lista

def is_valid_move(c, y, x):    
    pawn = b[y][x]
    if pawn.isdam==True:
        if can_capture_up(c, y, x):
            return True

        if can_capture_down(c, y, x):
            return True

    else:
        if c=="W":
            if can_capture_up(c, y, x):
                return True
        if c=="B":
            if can_capture_down(c, y, x):
                return True
    return False 

def can_jump_down(y):
    if(y + 2 < GRID_SIZE):
        return True
    else:
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

def can_capture_up(c,y,x):
    if(can_jump_up(y)):
        if(can_jump_left(x)):
            if(b[y - 1][x - 1] != None and b[y - 1][x - 1].color !=c):
                if(b[y - 2][x - 2] == None):
                    return True

        if(can_jump_right(x)):
            if(b[y - 1][x + 1] != None and b[y - 1][x + 1].color !=c):
                if(b[y - 2][x + 2] == None):
                    return True

def can_capture_down(c,y,x):
    if can_jump_down(y):
        if(can_jump_left(x)):
            if(b[y + 1][x - 1] != None and b[y + 1][x - 1].color !=c):
                if(b[y + 2][x - 2] == None):
                    return True

        if(can_jump_right(x)):
            if(b[y + 1][x + 1] != None and b[y + 1][x + 1].color !=c):
                if(b[y + 2][x + 2] == None):
                    return True

def check_win(c):
    pawnlist=[]
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if b[y][x] != None and b[y][x].color ==c:
                    pawnlist.append(c)
    
    if c=="B":
        if len(pawnlist)==0:
            print("White wins")
            #end=datetime.datetime.now().time
            global Game_running
            Game_running=True
            return
    if c=="W":
        if len(pawnlist)==0:
            print("Black wins")
            #end=datetime.datetime.now().time
            Game_running=False
            return
    
    return pawnlist

def print_availiable_moves(c):
    lista=check(c)
    if c=="W":
        print("White's turn")
        if len(lista)>0:
            for pawn in lista:
                print("Availiable moves", end="")
                print(chr(pawn[1] + 65) + str(pawn[0]))
    if c=="B":
        print("Black's turn")
        if len(lista)>0:
            for pawn in lista:
                print("Availiable moves", end="")
                print(chr(pawn[1] + 65) + str(pawn[0]))
    return lista

def main():
    global Game_running
    Game_running=True
    while Game_running:
        #   White move
        print_board(b)
        c="W"
        pawnlist=check_win(c)
        lista=print_availiable_moves(c)
        move_pawn(lista,c)
        pawnlist=check_win(c)
        #   Black move

        print_board(b)
        c="B"
        pawnlist=check_win(c)
        lista=print_availiable_moves(c)
        move_pawn(lista,c)
        pawnlist=check_win(c)
main()
