# Importing
import logging  # logger

import coloredlogs # colored logs
 
from Coach import Coach # coach of nn
from localchess.ChessGame import ChessGame as Game # chess logic
from localchess.keras.NNet import NNetWrapper as nn # neural net
from utils import *

import sys # sys

log = logging.getLogger(__name__) # logger

coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.

args = dotdict({
    'numIters': 1000,
    'numEps': 1,              # Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 15,        #
    'updateThreshold': 0.55,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 50,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 1,         # Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,
    'showing_board': False,       # Showing board in self-play?

    'checkpoint': './temp/',    # checkpoint directory
    'load_model': False, # load model?
    'load_folder_file': ('./','best.pth.tar'), # directory to load file
    'numItersForTrainExamplesHistory': 20, # num of iterations for train examples

})


def main():
    """MAin function"""
    log.info('Loading %s...', Game.__name__) # loading iter [ITER]
    g = Game() # game

    log.info('Loading %s...', nn.__name__) # loading [NAME]
    nnet = nn(g) # neural net

    if args.load_model:
        log.info('Loading checkpoint "%s/%s"...', args.load_folder_file)
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
    else:
        log.warning('Not loading a checkpoint!')

    log.info('Loading the Coach...')
    c = Coach(g, nnet, args)

    if args.load_model:
        log.info("Loading 'trainExamples' from file...")
        c.loadTrainExamples()

    log.info('Starting the learning process 🎉')
    c.learn()


if __name__ == "__main__":
    main()
