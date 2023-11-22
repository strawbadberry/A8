import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board):
        pass

class HumanPlayer(Player):
    def get_move(self, board):
        return map(int, input(f"Enter the position (x,y) for {self.symbol}, separated by a comma: ").split(","))

class BotPlayer(Player):
    def get_move(self, board):
        empty_spots = [(x, y) for x in range(3) for y in range(3) if board[x][y] is None]
        return random.choice(empty_spots) if empty_spots else (0, 0)

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [[None] * 3 for _ in range(3)]
        self.players = [player1, player2]
        self.current_player_index = 0

    def play_turn(self):
        x, y = self.players[self.current_player_index].get_move(self.board)
        if 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] is None:
            self.board[x][y] = self.players[self.current_player_index].symbol
            self.current_player_index = 1 - self.current_player_index
        else:
            print("Invalid move, try again.")

    def get_winner(self):
        for i in range(3):
            if all(self.board[i][j] == self.board[i][0] for j in range(3)) and self.board[i][0] is not None:
                return self.board[i][0]
            if all(self.board[j][i] == self.board[0][i] for j in range(3)) and self.board[0][i] is not None:
                return self.board[0][i]

        if all(self.board[i][i] == self.board[0][0] for i in range(3)) and self.board[0][0] is not None:
            return self.board[0][0]
        if all(self.board[i][2 - i] == self.board[0][2] for i in range(3)) and self.board[0][2] is not None:
            return self.board[0][2]

        return None

    def is_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)

    def display_board(self):
        for row in self.board:
            print(' | '.join([' ' if cell is None else cell for cell in row]))
            print('-' * 9)
