from deck_creation import Character, char_list
import random as random

player1_hand = []

player2_hand = []


def hand_shuffle():
    """the size parameter will determine how many cards will be given to each player,
    if it is an invalid number,a try except statement should be included"""

    # We need a way to keep count of how many characters exist

    deck_size = []

    for i in range(len(char_list)):
        deck_size.append(i)

    for i in range(len(deck_size) // 2):
        index = random.choice(deck_size)
        player1_hand.append(char_list[index])
        deck_size.remove(index)

    for i in range(len(deck_size)):
        index = random.choice(deck_size)
        player2_hand.append(char_list[index])
        deck_size.remove(index)

    # Make sure that we're able to deal cards evenly
