from deck_creation import *
from hand_dealing import *

player1_names = []

player2_names = []


# We can then use getters and setters to get  the values and change the HP values as needed

def hand_development():
    # Get Names of Characters in a List
    for character in range(len(player1_hand)):
        character_name = player1_hand[character].name
        player1_names.append(character_name)

    for character in range(len(player2_hand)):
        character_name = player2_hand[character].name
        player2_names.append(character_name)

    return player1_names, player2_names


def update_hand(p1, p2):
    player1_hand.pop(p1 - 1)
    player2_hand.pop(p2 - 1)
    return


def combat(p1_choice, p2_choice):
    player1 = player1_names[p1_choice - 1]
    player2 = player2_names[p2_choice - 1]
    print("Player 1 has chosen to summon: ", player1)

    print("Player 2 has chosen to summon: ", player2)

    # The moment we've all been waiting for, the actual combat.

    player1_char = player1_hand[p1_choice - 1]
    player2_char = player2_hand[p2_choice - 1]

    # Could we have a method that checks for if something is dead??

    print("Player 1 Element: ", player1_char.element)
    print("Player 2 Element: ", player2_char.element)

    # This could also be traits

    while True:

        print("Player 1 HP: ", player1_char.health)
        print("Player 2 HP: ", player2_char.health)

        # Player 1 keeps reusing the same character so we get negative HP moment

        # Maybe have a function here that multiplies how much damage it does, it could be a variable we multiply
        # we can make a multiplier and multiply it and use it for these battle calculations and mention if its super
        # effective and also introduce that people can have a chance of having multiply types

        player1_char.health -= player2_char.attack
        player2_char.health -= player1_char.attack

        if player1_char.health <= 0 or player2_char.health <= 0:
            print("Player 1 HP: ", player1_char.health)
            print("Player 2 HP: ", player2_char.health)
            if player1_char.health > player2_char.health:
                # Probably want to have a check to make sure we dont output any negative values, so maybe we could
                # use isDead
                winner = "Player 1"
                print("The Winner is: ", winner)
                return winner

            if player2_char.health > player1_char.health:
                winner = "Player 2"
                print("The Winner is: ", winner)
                return winner
            else:
                print("It's a tie!")

                break

            # NOw we need a way to make the combat slower (i.e turn based, and at the same time we should use all the

            # characters until we determine a final winner, also remove dead chars from summoning list

    # Include an option for user to input their name I think that'd be rossome

    # Incorporate a mana feature and cost for cards as well!!! That would also be cool methinks

    # How can I keep this loop going until someone dies? Maybe set a boolean value to see if a character is dead?
