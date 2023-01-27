    #dfs function for running dfs in the matrix
def dfs(board,i,j,m,n):
        if(i==-1 or j==-1 or i==m or j==n):
            return 
        elif(board[i][j]=='X'):
            return 
        elif(board[i][j]=='-1'):
            return 
        elif(board[i][j]=='O'):
            board[i][j]='-1'
            #dfs for next row
            dfs(board,i+1,j,m,n)
            #dfs for previous row
            dfs(board,i-1,j,m,n)
            #dfs for next column
            dfs(board,i,j+1,m,n)
            #dfs for previous column
            dfs(board,i,j-1,m,n)
            return

        
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

m=len(board)
n=len(board[0])
#check for every cell in outer spiral for 'O'
for i in range(m):
    for j in range(n):
        if(i==0 or i==m-1 or j==0 or j==n-1 and board[i][j]=='O'):
            #if found run dfs
            dfs(board,i,j,m,n)

#now every '0' is present it's inside the matrix and bounded by X's so replace them

for i in range(m):
    for j in range(n):
        if(board[i][j]=='O'):
            board[i][j]='X'
#now every '-1' is present on boundry has to be replaced by O
for i in range(m):
    for j in range(n):
        if(board[i][j]=='-1'):
            board[i][j]='O'

#print the board
for i in range(m):
    for j in range(n):
        print(board[i][j],end=' ')
    print()
        


