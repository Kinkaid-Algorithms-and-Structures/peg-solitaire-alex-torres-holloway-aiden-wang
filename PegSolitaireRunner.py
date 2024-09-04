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
        game_board.create_board()
        while not game_board.game_over():
            game_board.print_board()
            print("")
            peg_to_move = input("What peg do you want to move? ").capitalize()
            place_to_move = input("What place do you want to move to? ").capitalize()
            Board.is_legal_move(game_board, peg_to_move, place_to_move)



if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()
