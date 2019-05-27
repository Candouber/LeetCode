def fun(l):
	row = [{} for i in range(9)]
    matrix = [{} for i in range(9)]
    col = [{} for i in range(9)]
    for x in range(9):
        for y in range(9):
            temp =  board[x][y]
            num = (3*(x//3)+y//3)
            if temp != '.':
                if temp not in row[x] and temp not in col[y] and temp not in matrix[num]:
                    row[x][temp] = 1
                    col[y][temp] = 1
                    matrix[num][temp] = 1
                else:
                    return False
                
    return True