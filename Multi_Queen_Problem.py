n = 5
counter = 0
board = [[0 for p in range(n)] for q in range(n)]

def update_attack (board, n,i,j):
    attack = [[0 for p in range(n)] for q in range(n)]
    for x in range(n) :
        for y in range(n):
            if (board[x][y]==1):
                for temp in range(n):
                    #attack vertical
                    attack[temp][y] = 1
                    #attack horizontal
                    attack[x][temp] = 1
                    #diagnal top left to bottom right
                    if(((temp+x)<n) and ((temp+y)<n)):
                        attack[x+temp][y+temp]=1
                    if(((x-temp)>=0) and ((y-temp)>=0)):
                        attack[x-temp][y-temp]=1
                    #diagnal top right to bottom left
                    if(((temp+x)<n) and ((y-temp)>=0)):
                        attack[x+temp][y-temp]=1
                    if(((x-temp)>=0) and ((temp+y)<n)):
                        attack[x-temp][y+temp]=1
    if attack[i][j] == 0:
        return False
    else:
        return True
    
def play (board1,count,n, counter) :
    for i in range(n) :
        for j in range(n):
            if update_attack(board1,n,i,j) == False:
                board1[i][j] = 1
                count +=1
                if count == n:
                    counter +=1
                    print ("Solution " + str(counter))
                    for row in board1:
                        print(row)
                    print("\n")
                    return counter
                counter = play(board1,count,n, counter)
    return counter
                
for i in range(int(n/2)) :
    for j in range(int(n/2)):
        board[i][j] = 1
        counter = play (board, 1, n, counter)
        board = [[0 for p in range(n)] for q in range(n)]
