def print_grid(grid):
    for i in range(len(grid)):
        print('|'.join(grid[i]))
        if i<len(grid)-1:
            print('-'*5)

def get_player_move(player,grid):
    while True:
        try:
            move=input(f"Player {player}, Enter two integers separated by space")
            row,col=move.split()
            row=int(row)
            col=int(col)
            if row<0 or row>2 or col<0 or col>2:
                print("Invalid Input, Row and Col must be between 0 and 2")
                continue
            if grid[row][col]!=" ":
                print("The cell is already taken, Choose another")
                continue
            return row, col
        except ValueError:
            print('Invalid Input , Enter two integers separated by space')
            
def update_grid(grid,row,col,player):
    grid[row][col]=player

def check_winner(grid,player):
    # check rows:
    for row in grid:
        if all(cell==player for cell in row):
            return True

    #check columns
    for col in range(3):
        if all(grid[row][col]==player for row in range(3)):
            return True
    #check diaginals
    if all(grid[i][i]==player for i in range(3)) or all(grid[i][2-i]==player for i in range(3)):
        return True

def check_draw(grid):
    return all(all(cell!=' ' for cell in row) for row in grid)

def main():
    grid=[[" " for _ in range(3)] for _ in range(3)]
    current_player='X'
    
    while True:
        print_grid(grid)
        row,col=get_player_move(current_player,grid)
        if grid[row][col]==' ':
            update_grid(grid,row,col,current_player)
            if check_winner(grid,current_player):
                print_grid(grid)
                print(f"Player {current_player} wins")
                break
            elif check_draw(grid):
                print(grid)
                print("It's a draw")
                break
            current_player='O' if current_player=='X' else 'X'
        else:
            print("Cell already taken. Choose another move")


if __name__=="__main__":
    main()




