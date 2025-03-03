# It's just an x-axis
# Dominant strategy is pick highest number

class Game:
    def __init__(self, board=0, player=1, winner=None):
        self.board = board
        self.player = player
        self.winner = winner

    def get_legal_moves(self):
        return [1, 2] if self.player == 1 else [-0.5, -1.5]

    def make_move(self, move):
        self.board += move
        self.player = -self.player
        self.winner = self.check_winner()

    def check_winner(self):
        if self.board >= 10:
            return 1
        elif self.board <= -10:
            return -1
        else:
            return 0

    def is_terminal(self):
        return self.winner is not None

    def get_reward(self):
        return self.winner

    def reset(self):
        self.board = 0
        self.player = 1
        self.winner = None

    def copy_state(self):
        return (self.board, self.player, self.winner)

    def render(self):
        print(f"Board: {self.board}, Player: {self.player}, Winner: {self.winner}")
