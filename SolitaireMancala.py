import random


class SolitaireMancala:
    # create a SolitaireMancala object whose configuration consists of a board with an empty stone and no houses
    def __init__(self):
        self.board = [0]

    # get the board to be a copy of the supplied configuration (to avoiding referencing issues).
    # The configuration will be a list of integers in the form described above.
    def set_board(self, configuration):
        self.board = configuration[:]

    # return a string corresponding to the current configuration of the Mancala board
    def __str__(self):
        return str(self.board[::-1])
        # ' '.join(str(e) for e in board)
        # str(self.board[::-1])

    # return the number of seeds in the house with index house_num
    # note that 0 corresponds to the store
    def get_num_seeds(self, house_num):
        return self.board[house_num]

    def convert_given_house_number(self, house_num):
        return 7 - house_num

    # return True if the number of seeds is equal to the index of the house.
    # Otherwise, return false. If the house_num is 0, return False also.
    def is_legal_move(self, house_num):
        return house_num == self.board[house_num] and house_num != 0

    # apply a legal move for house house_num to the board.
    def apply_move(self, house_num):
        if (self.is_legal_move(house_num)):
            # backwards iteration from n to 0
            # 1. for i in reversed(range(n+1))
            # 2. for i in range (n, -1, -1)
            for i in reversed(range(house_num + 1)):
                self.board[i] = self.board[i] + 1

            # eventually the number of seeds in that house will be 0
            self.board[house_num] = 0
        else:
            print("Illegal move!")

    # return the index for the legal move whose house is closet to the store. If no legal move is available, return 0.
    def choose_move(self):
        for i in range(1, 7):
            if (self.is_legal_move(i)):
                return i
        return 0

    # return True if all houses contain no seeds. Otherwise, return False.
    def is_game_won(self):
        for i in self.board:
            if (i != 0):
                return False
        return True

    # plan_moves(self) returns a list of legal moves based on the following heuristic: after each move, move the seeds in the house closest tp
    # the store when given a choice of legal moves. Should not update the current configuration of the game.
    def plan_moves(self):
        # list to store all valid moves so far
        legal_moves_list = []
        while (not self.is_game_won() and self.choose_move() != 0):
            legal_moves_list.append(self.choose_move())
            self.apply_move(self.choose_move())
        return legal_moves_list


if __name__ == '__main__':
    '''
    Test code for Solitaire Mancala
    '''
    my_game = SolitaireMancala()
    # print("1.Testing init - Computed: ", str(my_game), "Expected: ", str([0]))

    config1 = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(config1)
    print("2.Testing init - Computed: ", str(my_game), "Expected: ", str([0, 0, 1, 1, 3, 5, 0]))
    print("Testing get_num_seeds- Computed: ", my_game.get_num_seeds(1), "Expected: ", config1[1])
    print("Testing get_num_seeds- Computed: ", my_game.get_num_seeds(3), "Expected: ", config1[3])
    print("Testing get_num_seeds- Computed: ", my_game.get_num_seeds(4), "Expected: ", config1[4])

    print(str(my_game.plan_moves()))
