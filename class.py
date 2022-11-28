class TicTacBoard:
    def __init__(self):
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.field.append(r)

        self.move_x = True
        self.end_of_game = False
        self.winner = None
        self.win = ''
        self.first_move = True

    def new_game(self):
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.move_x = True
        self.end_of_game = False
        self.winner = None
        self.win = ''
        self.first_move = True

    def get_field(self):
        return self.field


    def check_field(self):
        if self.win == 'X':
            return 'X'
        elif self.win == '0':
            return 0
        else:
            return None


    def make_move(self, row, col):
        if self.end_of_game and not self.first_move:
            return 'Игра закончена'
        else:
            if self.field[row - 1][col - 1] != '-':
                return f'Клетка {row}, {col} занята'
            else:
                if self.move_x:
                    self.field[row - 1][col - 1] = 'X'
                    self.move_x = False
                    self.first_move = False
                else:
                    self.field[row - 1][col - 1] = '0'
                    self.move_x = True
                    self.first_move = False
                for i in range(2):
                    if (self.field[0][i] == self.field[1][i] == self.field[2][i]) and (self.field[0][i] != '-'):
                        self.end_of_game = True
                        self.win = self.field[0][i]
                        return f'Победил играк{self.field[0][i]}'
                    elif (self.field[i][0] == self.field[i][1] == self.field[i][2]) and (self.field[i][0] != '-'):
                        self.end_of_game = True
                        self.win = self.field[0][i]
                        return f'Победил играк{self.field[0][i]}'
                    elif (self.field[0][0] == self.field[1][1] == self.field[2][2]) and (self.field[0][0] != '-'):
                        self.end_of_game = True
                        self.win = self.field[0][0]
                        return f'Победил играк{self.field[0][0]}'
                    elif (self.field[0][2] == self.field[1][1] == self.field[2][0]) and (self.field[0][2] != '-'):
                        self.end_of_game = True
                        self.win = self.field[0][2]
                        return f'Победил играк{self.field[0][2]}'
                return 'Продолжаем играть'


board = TicTacBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")