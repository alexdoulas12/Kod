from pdb import set_trace
import datetime
class Pawn(object):#Skapar objekten pjäser med färg och drottningskap som attribut

    def __init__(self,color,isdam):
            self.color=color
            self.isdam=isdam
class Time(object):#Skapar tidsobjekt som används för highscorelistan
    def __init__(self, minutes, seconds, name, size):

        self.minutes = int(minutes)
        self.seconds = int(seconds)
        self.size = int(size)
        self.name = name
GRID_SIZE = 8
global Game_running
Game_running=True
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

def valid_move_from():#Kollar om den initiala pjäsen är inom brädet och av rätt form
    while True:
        try:
            p=input("Choose a pawn to move ").upper()

            if p=="QUIT":
                print("Shutting down")
                global Game_running
                Game_running=False
                global Outer
                Outer=False
                return Game_running, Outer
            
            x=int((ord(p[0])-65))
            if x>GRID_SIZE-1 or x<0:
                print("Choose a pawn in the form of: A5 B2 C9...")
                continue

            y=int(p[1])
            if y>GRID_SIZE-1 or y<0:
                print("Choose a pawn in the form of: A5 B2 C9...")
                continue
            elif len(p)>2:
                print("Choose a pawn in the form of: A5 B2 C9...")
                continue
            else:
                return p
        except IndexError:
            continue
        except ValueError:
           continue

def valid_move_to():#Kollar om rutan man flyttar till är inom brädet och av rätt form 
    while True:
        try:
            k=input("Choose a square to move to ").upper()
            if k=="QUIT":
                print("Shutting down")
                global Game_running
                Game_running=False
                return

            w=int((ord(k[0])-65))

            if w>GRID_SIZE-1 or w<0:
                print("Choose a pawn in the form of: A5 B2 C9...")
                continue

            z=int(k[1])
            
            if z>GRID_SIZE-1 or z<0:
                print("Choose a square in the form of: A5 B2 C9...")
                continue
            elif len(k)>2:
                print("Choose a square in the form of: A5 B2 C9...")
                continue
            else:
                return k
        except IndexError:
            continue
        except ValueError:
            continue

def move_pawn(lista,c):#Flyttar pjäsen utifrån färg och listan med tillgängliga drag
    capture_made=False
    global Outer
    Outer=True
    while Outer:
        p=valid_move_from()
        if Game_running==False:
            break
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
                                capture_made=True
                                check_for_queen(c, z, w)
                                break
                            if w==x+2:
                                b[z][w]=b[y][x]
                                b[z+1][w-1]=None
                                b[y][x]=None
                                Outer=False
                                capture_made=True
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
                            capture_made=True
                            check_for_queen(c,z,w)
                            break
                            
                        if w==x-2:
                            b[z][w]=b[y][x]
                            b[z-1][w+1]=None
                            b[y][x]=None
                            Outer=False
                            capture_made=True
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
                k=valid_move_to()
                if Game_running==False:
                    break
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
                                capture_made=True
                                check_for_queen(c,z,w)
                                break
                                
                            if w==x-2:
                                b[z][w]=b[y][x]
                                b[z-1][w+1]=None
                                b[y][x]=None
                                Outer=False
                                capture_made=True
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
                            capture_made=True
                            check_for_queen(c, z, w)
                            break
                        if w==x+2:
                            b[z][w]=b[y][x]
                            b[z+1][w-1]=None
                            b[y][x]=None
                            Outer=False
                            capture_made=True
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
        if capture_made:
            while (check_for_more_moves(c,lista,y,x,w,z)==True):   
                    another_move(c,lista)

def another_move(c,lista):#Utför ett andra drag om det är tillgängligt. Lik move_pawn
    lista=check(c)
    print("LISTA I ANOTHER MOVE:", lista)
    for pawn in lista:
            x=pawn[1]
            y=pawn[0]
            print("X,Y=",x,y)
            print(chr(pawn[1] + 65) + str(pawn[0]))

    if c=="B":
        while True:#Flyttar svart spelare
            k=valid_move_to()
            if Game_running==False:
                return
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
            k=valid_move_to()
            if Game_running==False:
                return
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

def check(c):#Kollar om det finns pjäser av färg c som har ett tillgängligt drag och lägger isåfall till de i en lista
    lista=[]
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if b[y][x] != None and b[y][x].color ==c:
                if(is_valid_move(c, y, x)):
                    lista.append([y, x])
    return  lista

def check_for_queen(c, z, w):#Kollar om en pjäs har nått andra sidan brädet och gör isåfall den till en drottning
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

def check_for_more_moves(c,lista,x,y,w,z):#Kollar om det finns mer tillgängliga drag för pjäsen som senast flyttades
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

def is_valid_move(c, y, x):#Kollar om man kan fånga en pjäs
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

def check_win(c):#Kollar om spelet vunnits
    pawnlist=[]
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if b[y][x] != None and b[y][x].color ==c:
                    pawnlist.append(c)

    if c=="B":
        if len(pawnlist)==0:
            print("White wins")
            Game_running=False
            return Game_running
    if c=="W":
        if len(pawnlist)==0:
            print("Black wins")
            Game_running=False
            return Game_running

def print_availiable_moves(c):#Skriver ut tillgängliga drag
    lista=check(c)
    if c=="W":
        print("White's turn")
        if len(lista)>0:
            for pawn in lista:
                print("Availiable moves ", end="")
                print(chr(pawn[1] + 65) + str(pawn[0]))
    if c=="B":
        print("Black's turn")
        if len(lista)>0:
            for pawn in lista:
                print("Availiable moves ", end="")
                print(chr(pawn[1] + 65) + str(pawn[0]))
    return lista

def valid_name_input():#Kollar att namnen är i bokstavsform
    while True:
            try:
                name=input("Write your first name ").capitalize()
                if name.isalpha():#Kollar om namnet består av bara bokstäver
                    if len(name)>=3:
                        return name
                    else:
                        print("Name must be at least three letters long")
                        continue
                else:
                    print("Name must consist of only letters and contain no spaces")
                    continue
            except:
                print("except")
                continue

def game_finished(start):#Funktion som skapar läser och skapar highscorefilen och "behandlar" den för input
    try:
        hiscores_file = open("hiscores.txt", "r")
    except FileNotFoundError:
        hiscores_file = open("hiscores.txt", "a+")#Skapar filen om den inte finns
    times = []

    for line in hiscores_file:#Tar ut delar av filen för sortering
        list_of_lines = line.split(" ")
        name = list_of_lines[1]
        minutes = list_of_lines[3][:-1]
        seconds = list_of_lines[4].rstrip()[:-2]
        size = list_of_lines[6].split("x")[0]
        time = Time(minutes, seconds, name, size)

        times.append(time)
    #   Creates a timeObject for the new player
    minutes,seconds=timekeep(start)#Tar in tiden då spelet avslutades
    name=valid_name_input()#Tar in namn på spelaren som sedan läggs till
    size=GRID_SIZE#Storleken av brädet
    Highscorelist(minutes, seconds, name, times, size)

def Highscorelist(minutes, seconds, name, times, size):#Skapar highscorelistan och sorterar den
    t = Time(minutes, seconds, name, size)
    times.append(t)

    times = sorted(times, key=lambda x: x.minutes)
    times = sorted(times, key=lambda y: y.size, reverse=True)
    str_to_file = ""

    for i, time in enumerate(times):
        str_to_file += str(i + 1) + ". " + time.name + " - " + str(time.minutes) + "m " + str(time.seconds) + "s. " + "- " + str(time.size) + "x" + str(time.size) + "\n"
    hiscores_file = open("hiscores.txt", "w")
    hiscores_file.write(str_to_file)

    hiscores_file.close()
    hiscores_file = open("hiscores.txt", "r")
    print(hiscores_file.read())

def timekeep(start):#Tar tiden
    end=datetime.datetime.now()#Tar in tiden då spelet avslutades
    tdelta=end-start
    minutes_total=tdelta.total_seconds()/60
    minutes=tdelta.total_seconds()//60#Delar antalet sekunder jämt på 60
    seconds=round((minutes_total-minutes)*60,2)#Kalkylerar antalet sekunder som blir kvar efter uträkningen av minuter och rundar av de till två decimaler
    return minutes,seconds

def print_intstructions():#Spelinstruktioner och val av spelarfärg
    print(" "*10,"CHECKERS\nRULES")
    print("1.You may only move diagonaly\n2.You capture an enemy piece by jumping over it\n3.When a pawn reaches the other side it becomes a queen and may move backwards")
    print("4.You may move as long as there is an availiable capture for the same pawn last moved\n5.The player that loses all of their pawns loses the game")
    print("\nOBJECTIVE: Capture all the enemy pawns in the shortest time for a place on the leaderboard")
    print("To exit the game at any time, write QUIT when prompted to move a pawn")
    while True:
        try:
            c_player=input("Choose a starting color, Black or White ").capitalize()
            if c_player=="Black" or c_player=="B":
                c_player="B"
                return c_player
            if c_player=="White" or c_player=="W":
                c_player="W"
                return c_player
        except:
            pass

def main():
    global Game_running
    Game_running=True
    c_player=print_intstructions()
    c=c_player
    start=datetime.datetime.now()#Tar in starttiden
    while Game_running:
        #   White move
        print_board(b)
        check_win(c)
        lista=print_availiable_moves(c)
        move_pawn(lista,c)
        check_win(c)
        if Game_running==True:
            if c=="W":
                c="B"
            else:
                c="W"
        
    else:
        game_finished(start)
       
        print("You lose")

main()
