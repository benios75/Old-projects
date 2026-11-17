table = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]
game = True
draw = False

def tablePrint():
    for i in range(3):
        print(table[i])
def ifWin():
    
    
    global whoWins
    global winType
    #X wins

    #Row win
    if (table[0][0]=="X" and table[0][1]=="X" and table[0][2]=="X") or (table[1][0]=="X" and table[1][1]=="X" and table[1][2]=="X") or (table[2][0]=="X" and table[2][1]=="X" and table[2][2]=="X"):
        winType = "row"
        whoWins = "X"
        return False 
    #Column Win   
    elif (table[0][0]=="X" and table[1][0]=="X" and table[2][0]=="X") or (table[0][1]=="X" and table[1][1]=="X" and table[2][1]=="X") or (table[0][2]=="X" and table[1][2]=="X" and table[2][2]=="X"):
        winType = "column"
        whoWins = "X"
        return False
    #Slant win
    elif (table[0][0]=="X" and table[1][1]=="X" and table[2][2]=="X") or (table[0][2]=="X" and table[1][1]=="X" and table[2][0]=="X"):
        winType = "slant"
        whoWins = "X"
        return False
    
    #O wins

    elif (table[0][0]=="O" and table[0][1]=="O" and table[0][2]=="O") or (table[1][0]=="O" and table[1][1]=="O" and table[1][2]=="O") or (table[2][0]=="O" and table[2][1]=="O" and table[2][2]=="O"):
        winType = "row"
        whoWins = "O"
        return False    
    #Column Win   
    elif (table[0][0]=="O" and table[1][0]=="O" and table[2][0]=="O") or (table[0][1]=="O" and table[1][1]=="O" and table[2][1]=="O") or (table[0][2]=="O" and table[1][2]=="O" and table[2][2]=="O"):
        winType = "column"
        whoWins = "O"
        return False
    #Slant win
    elif (table[0][0]=="O" and table[1][1]=="O" and table[2][2]=="O") or (table[0][2]=="O" and table[1][1]=="O" and table[2][0]=="O"):
        winType = "slant"
        whoWins = "O"
        return False
    else:
        return True
def ifDraw():
    gut = False
    for row in table:
        for place in row:
            if place==' ':
                gut = True
    if gut==True:
        return True
    else: 
        return False
tablePrint()
#Game loop
while game:
    #Coordinates reset for X
    x = 0
    y = 0
    
    #Putting X
    while True:
        while True:
            x = input("Row of an X(1,2,3): ")
            if x=="1" or x=="2" or x=="3":
                break
            else:
                print("You must choose 1, 2 or 3!")
        x = int(x)-1
        while True:
            y = input("Column of an X(1,2,3): ")
            if y=="1" or y=="2" or y=="3":
                break
            else:
                print("You must choose 1, 2 or 3!")
        y = int(y)-1
        if table[x][y] ==" ":
            break
        else:
            print("This place is ocuupied!")
    
    table[x][y] = "X"

    #Coordinates reset for O
    x = 0
    y = 0


    tablePrint()
    game = ifWin() 
    if game==False:
        break
    game = ifDraw() 
    if game==False:
        draw = True
        break

    #Putting O
    while True:
        while True:
            x = input("Row of an O(1,2,3): ")
            if x=="1" or x=="2" or x=="3":
                break
            else:
                print("You must choose 1, 2 or 3!")
        x = int(x)-1
        while True:
            y = input("Column of an O(1,2,3): ")
            if y=="1" or y=="2" or y=="3":
                break
            else:
                print("You must choose 1, 2 or 3!")
        y = int(y)-1    
        if table[x][y] ==" ":
            break
        else:
            print("This place is ocuupied!")
        
    table[x][y] = "O"
    tablePrint()
    game = ifDraw() 
    if game==False:
        draw = True
        break
    game = ifWin()

#End of the game
if draw:
    print("Its draw!")
else:
    print(f"{whoWins} Wins by {winType}!")

