from enum import IntEnum, auto

# Starter code

# See https://docs.python.org/3/library/enum.html#enum.IntEnum
class State(IntEnum):
    START = 0
    SELECT_CLASS = auto()
    SELECT_WEAPON = auto()

    LOOP_DEFAULT = auto()
    # LOOP_...


"""
Main game
"""
def game():
    running = True

    state = State.START

    # TODO: Print start message

    while running:
        user_input = input("> ").lower()

        if user_input == "quit":
            running = False
        
        else:
            print(user_input)
        
        # TODO: Select character name, class, weapon, etc
        # TODO: Battle

if __name__ == "__main__":
    game()