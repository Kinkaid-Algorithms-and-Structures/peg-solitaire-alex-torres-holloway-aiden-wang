import logging, datetime
from KinkaidDecorators import log_start_stop_method
from Board import Board
from Peg import Peg

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]

class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing.")

        # add any code you want to set up variables for the game.
    
    @log_start_stop_method
    def play_game(self):  # note: this is complaining (grey underline) that it could be static because it doesn't use
        # any variables or methods from "self." Once you do, it will stop pestering you about it.
        game_board = Board()
        game = True
        game_board.create_board()
        print("Welcome to peg solitaire!")
        print("The pluses are pegs, and the circles are holes.")
        while game:
            game_board.print_board()
            while True:
                cur_row, cur_col = input("\nRow and column of peg to move, separated by spaces (start from 0 and spaces don't count) ").split()
                to_row, to_col = input("Row and column of place to move to, separated by spaces (start from 0 and spaces don't count) ").split()
                if not game_board.in_bounds(cur_row, cur_col) or not game_board.in_bounds(to_row, to_col):
                    print("Move out of bounds. Try another move.")
                    continue
                if game_board.is_legal_move(game_board.get_peg(cur_row, cur_col), game_board.get_peg(to_row, to_col)):
                    break
            game_board.move(game_board.get_peg(cur_row, cur_col), game_board.get_peg(to_row, to_col))
            game_board.remove(game_board.get_peg(cur_row, cur_col), game_board.get_peg(to_row, to_col))
            print("Good move!")
            if game_board.each_has_neighbors == False and game_board.get_peg_count > 1:
                game = False
                print("You lost!")
            if game_board.get_peg_count == 1:
                game = False
                print("You won!")

if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()
