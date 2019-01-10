from room import Room
from player import Player
from item import Item
# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter the name of your character: ")
player = Player(player_name)
player.room = room['outside']



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(f"{player.name}, you are in the {player.name.room}")
print(f"{player.room.description}")

prompt(
    f"""Commands:
    Press N to go north.
    Press E to go east.
    Press S to go south.
    Press W to go west.
    press q to quit."""
)

while True:
    action = input("What is your next move? ").lower()

    if action == 'n':
        try:
            player.room = player.room.n_to
        except AttributeError:
            print("You can not move that direction.  Try again.")
    elif action == 'e':
        try:
            player.room = player.room.e_to
        except AttributeError:
            print("You can not move that direction.  Try again.")
    elif action == 's':
        try:
            player.room = player.room.s_to
        except AttributeError:
            print("You can not move that direction.  Try again.")
    elif action == 'w':
        try:
            player.room = player.room.w_to
        except AttributeError:
            print("You can not move that direction.  Try again.")



