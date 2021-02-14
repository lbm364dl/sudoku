from time import time

def get_input():
    with open("sudoku.txt") as f:
        inp = list(filter(lambda x: x[0]!='G', f.read().splitlines()))
        grids = []
        for i in range(0, len(inp), 9):
            grids.append([[int(c) for c in i] for i in inp[i:i+9]])
    return grids


def get_grid(grid):
    text = ''
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            text += ('| ' if j==3 or j==6 else '')+str(col)+' '
        text += '\n---------------------\n' if i==2 or i==5 else '\n'

    return text


def get_row(grid, i):
	return grid[i]


def get_col(grid, j):
    return [row[j] for row in grid]


def get_box(grid, i, j):
    row_box = 3 * (i // 3);
    col_box = 3 * (j // 3);
    return [col for row in grid[row_box:row_box + 3] for col in row[col_box:col_box + 3]]


def is_num_valid(grid, num, i, j):
    #print(f'Checking {num} in position ({i},{j})')
    return num not in get_row(grid, i) and num not in get_col(grid, j) and num not in get_box(grid, i, j)

def empty_squares(grid):
	l = [(i, j) for i, row in enumerate(grid) for j, col in enumerate(row) if col == 0]
	print(81-len(l))
	return l

def solve(grid, empty):
	#print(i, j, grid[0][1])

	if empty == []: 
		return grid

	i, j = empty[0]	

	num = 1
	res = None
	while res == None and num < 10:
		if is_num_valid(grid, num, i, j):
			grid[i][j] = num
			res = solve(grid, empty[1:])

			#if res != None:
			#	print(i, j, "skajdaks")
			#	print(get_grid(grid))
		
		num += 1

	if res == None:
		grid[i][j] = 0
	return res 
	

def check_solution(grid):
	for i in range(9):
		assert(len(set(get_row(grid, i))) == 9)
		assert(len(set(get_col(grid, i))) == 9)

	for i in range(0,9,3):
		for j in range(0,9,3):
			assert(len(get_box(grid, i, j)) == 9)
	   

start = time()
grid = [[0, 2, 4, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 7, 1, 0, 0], 
 [0, 9, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 8, 4],
 [0, 0, 0, 0, 7, 5, 0, 0, 0], 
 [6, 0, 0, 0, 3, 0, 0, 0, 0], 
 [0, 0, 0, 4, 0, 0, 0, 2, 9], 
 [0, 0, 0, 2, 0, 0, 3, 0, 0], 
 [1, 0, 0, 0, 0, 0, 0, 0, 0]]

print(get_grid(grid))
print(get_grid(solve(grid, empty_squares(grid))))

#grids = get_input()
#
#i = 0
#for grid in grids:
#	i += 1
##	print(i)
#	#print(get_grid(grid))
#	res = solve(grid, empty_squares(grid))
#	#print(get_grid(res))
#	#check_solution(res)
#
end = time()
print(end-start)
