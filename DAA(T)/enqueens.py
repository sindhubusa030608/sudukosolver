def safe(board,row,col,n):
    for i in range(row):
        if board[i]==col:
            return False
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if board[i]==j:
            return False
        i=i-1
        j=j-1

    i=row-1
    j=col+1
    while i>=0 and j<=n:
        if board[i]==j:
            return False
        i=i-1
        j=j-1
def solve(board,row,n):
    if row==n:
        print(board)
        return
    for col in range(n):
        if safe(board,row,col,n):
            board[row]=col
            solve(board,row+1,n)
n=4
board=[-1]*n
solve(board,0,n)
    i
