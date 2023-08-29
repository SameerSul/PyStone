from deck_creation import Character
from hand_dealing import hand_shuffle
from PreCombat import hand_development, combat, update_hand

# Hearthstone Project

""" So for this project we are going to need the following functions, a dictionary or list which will record all the
possible monsters a user can have and the damage values associated with each. A system which
deals out these cards accordingly to the user and keeps track of their hands. A system which will allow users to play
these cards (hopefully with summoning conditions) and a system which will conduct damage calculations to determine a
winner.



As we move on, we can make the game more complicated and introduce more visuals, but for the time being,

let this be our project to get back into Python and get that fucking ball rolling and never make it stop

I don't want to fuck around anymore I wanna get shit DONE """


def main():
    # Deal out cards and instantiate characters

    # Work out this silly business later

    hand_shuffle()

    # Dealing out hands, yknow the bizz

    player1_hand, player2_hand = hand_development()

    # I think I should make this infinite and check for errors, so...... we'll work on that.

    # Turn and point tracker
    turns = 1
    p1_points = 0
    p2_points = 0

    # Run a for loop until all characters have been used
    while p1_points < 3 and p2_points < 3:
        print("It is now Turn: ", turns)
        print("Player 1 your hand is now: ", player1_hand)
        print("Player 2 your hand is now: ", player2_hand)
        player1_choice = int(input("Player 1, please summon a character by typing in a number <= length of list: "))
        player2_choice = int(input("Player 2, please summon a character by inputting a number <= length of list: "))
        # Taking in user input to determine what to summon
        winner = combat(player1_choice, player2_choice)
        # My main issue is to remove already used characters, bcs then otherwise I get -ive values and index errors
        # If we don't then we need to worry about the issue of negative numbers
        if winner == "Player 1":
            p1_points += 1
            if p1_points == 3:
                print("Player 1 Wins!")

        elif winner == "Player 2":
            p2_points += 1
            if p2_points == 3:
                print("Player 2 Wins")
        else:
            p2_points += 1
            p1_points += 1
            if p2_points == 3:
                print("Player 2 Wins")
            elif p1_points == 3:
                print("Player 1 Wins")



        player1_hand.pop(player1_choice - 1)
        player2_hand.pop(player2_choice - 1)

        update_hand(player1_choice,player2_choice)

        # We can use a counter that adjusts the index after each iteration to avoid index errors in precombat.py

        print("Player 1 pts: ", p1_points)
        print("Player 2 pts: ", p2_points)

        turns += 1

    # Give users the chance to play their cards, player 1 then player 2, eventually we allow spells too

    # Force them to fight and conduct battle calculations because I'm mean like that

    # Keep repeating until a winner is decided, later we can add multiple moves


print()

if __name__ == '__main__':
    main()
