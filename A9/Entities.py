
class Board:
    def __init__(self):
        self.__board=[[' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                      [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                      [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                      [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                      [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                      [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                      [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                      ]
        self.__moves_made=0

    def __str__(self):
        table_string=""
        for i in range(6):
            table_string+="|"
            for j in range(7):
                table_string+=self.__board[i][j]
                table_string += "|"
            table_string+='\n'
        return table_string

    def make_move(self,row:int,p:int):
        '''
        method that allows the player to make a move on the board
        :param row: row that the player chose
        :param p: helps identify the player that made the move: odd number - player 1
                                                                 even number - player 2
        '''
        try:
            if self.possible_move(row):
                if self.__board[5][row] == ' - ':
                    if p % 2 == 0:
                        self.__board[5][row] = '🔴 '
                    else:
                        self.__board[5][row] = '🔵 '

                else:
                    for i in range(6):
                        if self.__board[i][row]!=' - ':
                            if p%2==0:
                                self.__board[i - 1][row] = '🔴 '
                                break
                            else:
                                self.__board[i - 1][row] = '🔵 '
                                break
                p+=1

            else:
                if not self.check_win(p):
                    return "Game is won!"
                if self.is_table_full():
                    exception = RowFullException("Row is full")
                    raise exception
        except:
            pass

    def is_table_full(self):
        if self.__moves_made==42:
            return True
        return False

    def possible_move(self,row):
        if self.__board[0][row] != ' - ':
            return False
        else:
            return True
    def start_game(self):
        pass

    def check_win(self, player):
        if player %2 == 1:
            piece = "🔵"
        elif player%2 == 0:
            piece = "🔴"
        for x in range(3):
            for y in range(7):
                if (self.board[x][y] == piece and self.board[x + 1][y] == piece and self.board[x + 2][
                    y] == piece and self.board[x + 3][y] == piece):
                    return True

        # Check for horizontal win
        for x in range(6):
            for y in range(4):
                if (self.board[x][y] == piece and self.board[x][y + 1] == piece and self.board[x][
                    y + 2] == piece and self.board[x][y + 3] == piece):
                    return True

        for x in range(3):
            for y in range(4):
                if (self.board[x][y] == piece and self.board[x + 1][y + 1] == piece and self.board[x + 2][
                    y + 2] == piece and self.board[x + 3][y + 3] == piece):
                    return True
        for x in range(3):
            for y in range(3, 7):
                if (self.board[x][y] == piece and self.board[x + 1][y - 1] == piece and self.board[x + 2][
                    y - 2] == piece and self.board[x + 3][y - 3] == piece):
                    return True

        return False

class ExceptionClass:
    def __init__(self,message):
        self._m=message
    def __str__(self):
        return self._m

class RowFullException(ExceptionClass):
    pass


board = Board()
board.make_move(1,1)
board.make_move(1,2)
board.make_move(1,3)
board.make_move(1,4)
board.make_move(1,5)
board.make_move(1,6)
board.make_move(1,7)
board.make_move(0,9)
board.make_move(2,11)
board.make_move(3,13)
board.make_move(4,14)

print(board)
