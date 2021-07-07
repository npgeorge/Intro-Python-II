from room import Room
from player import Player

# Day 1 MVP
# Create the input command parser in adv.py which allows the 
# program to receive player input and commands to move to 
# rooms in the four cardinal directions.

# Declare all the rooms

room = {
    'outside':  Room("Outside the Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("on the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
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
player1 = Player('Nick', room['outside'])
print(f"Hello {player1.name}, You are located {player1.current_room.name}")

# * Prints the current room name
print(f"You are located: {player1.current_room.name}")
# * Prints the current description (the textwrap module might be useful here).
print(f"You are located: {player1.current_room.description}")
# * Waits for user input and decides what to do.
    #user chooses a direction
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    #user_input = input("Choose a cardinal direction or enter q to quit:\n")
turn_off = False

while not turn_off:
    print(f"Hello {player1.name}, You are located {player1.current_room.name}")
    print(f"Where are you? Where might you go? {player1.current_room.description}")
    print(f"You have {player1.current_room.item_list} contents in your room.")

    compass_in = input("Enter a direction to travel next! (n,s,e,w)>")
    compass_split = compass_in.split(' ')

    if len(compass_split) == 1:
        if compass_in == 'n':  
            if player1.current_room.n_to == None:
                print("Uh oh! This direction leads no where! Try again!")
                player1.current_room
            else:
                player1.current_room = player1.current_room.n_to
        elif compass_in == 's':
            if player1.current_room.s_to == None:
                print("Uh oh! This direction leads no where! Try again!")
                player1.current_room
            else:
                player1.current_room = player1.current_room.s_to
        elif compass_in == 'e':
            if player1.current_room.e_to == None:
                print("Uh oh! This direction leads no where! Try again!")
                player1.current_room
            else:
                player1.current_room = player1.current_room.e_to
        elif compass_in == 'w':
            if player1.current_room.w_to == None:
                print("Uh oh! This direction leads no where! Try again!")
                player1.current_room
            else:
                player1.current_room = player1.current_room.w_to
        elif compass_in == 'i' or 'inventory':
            print(player1.inventory)
        elif compass_in == 'q':
            print("Game Over!")
            turn_off = True
    elif len(compass_split) == 2:
        if compass_split[0] == 'get' or 'take':
            for x in player1.current_room.item_list:
                if x.name == compass_split[1]:
                    player1.current_room.item_list.remove(x)
                    player1.inventory.append(x)
                    x.on_take()
                else:
                    print(f"There is no {compass_split[1]} in this room.")
        if compass_split[0] == 'drop':
            for y in player1.inventory:
                if y.name == compass_split[1]:
                    player1.inventory.remove(y)
                    player1.current_room.item_list.append(y)
                    y.on_drop()
                else:
                    print(f"You don't have {compass_split[1]} in your satchel.")
    else:
        print("You must choose to enter a direction or get/take an item")