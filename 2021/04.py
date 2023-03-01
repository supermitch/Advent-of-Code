with open('04_input.txt') as f:
    data = [x.strip() for x in f]

called = [int(x) for x in data[0].split(',')]

row_boards = []
for i in range(2, len(data) - 4, 6):
    row_b = []
    for j in range(5):
        line = data[i + j]
        row_b.append([int(x) for x in line.split()])
    row_boards.append(row_b)

col_boards = []
for r_b in row_boards:
    col_b = []
    for i in range(5):
        col = []
        for row in r_b:
            col.append(row[i])
        col_b.append(col)
    col_boards.append(col_b)


def play_game(called, row_boards, col_boards):
    for num in called:
        for i, board in enumerate(row_boards):
            for j, row in enumerate(board):
                if num in row:
                    row = [x for x in row if x != num]
                    board[j] = row
                    if not row:
                        return i, num, board

        for i, board in enumerate(col_boards):
            for j, col in enumerate(board):
                if num in col:
                    col = [x for x in col if x != num]
                    board[j] = col
                    if not col:
                        return i, num, board


i, num, board = play_game(called, row_boards, col_boards)

total = sum(sum(row) for row in board)
print(f'Part A: The winning board score is {total * num}')


def lose_game(called, row_boards, col_boards):
    while True:
        i, num, board = play_game(called, row_boards, col_boards)
        row_boards.pop(i)
        col_boards.pop(i)
        if not row_boards:  # The last board just ended
            return num, board


num, board = lose_game(called, row_boards, col_boards)

total = sum(sum(row) for row in board)
print(f'Part B: The losing board score is {total * num}')
