#!/bin/python3 -tt

# Author: Fº Javier Gutierrez-Maturana Sanchez
# 
# Description: This program play bingo, 
# each player has only one cartoon.

import random
from Carton import Carton

MAX_NUMBERS = 5
MAX_VALUE = 90
MAX_LINES = 3
NUMBERS_LIST = tuple(range(1, MAX_VALUE + 1))

def main():
    cartoons = []

    cartoons.append(Carton(MAX_LINES, MAX_NUMBERS, MAX_VALUE))
    cartoons.append(Carton(MAX_LINES, MAX_NUMBERS, MAX_VALUE))
    cartoons.append(Carton(MAX_LINES, MAX_NUMBERS, MAX_VALUE))
    cartoons.append(Carton(MAX_LINES, MAX_NUMBERS, MAX_VALUE))

    # print("Bingo numbers!\n{}".format(NUMBERS_LIST))

    # print("---- Show perfects Cartoons ----")
    # for i in range(len(cartoons)):
    #    print ("Carton {}".format(i))
    #    cartoons[i].debug_cartoon(0)
    # print("--------------------------------")

    bingo = False
    winner = -1
    while not bingo:
        number = random.randint(1, MAX_VALUE)
        # print ("Number! {}".format(number))
        for player in range(len(cartoons)):
            cartoons[player].markNumber(number)

            if cartoons[player].hasLine():
               print("Player {} Line!".format(player))

            if cartoons[player].hasBingo():
                winner = player
                bingo = True
                break # Only one winner

    if winner >= 0:
        print("Game finish Bingo! Player {}".format(winner))

if __name__ == "__main__":
    main()
