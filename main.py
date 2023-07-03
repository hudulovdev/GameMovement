import random

# Game Constants
WIDTH = 10
HEIGHT = 10

# Player Constants
PLAYER_ICON = "P"
PLAYER_START_X = random.randint(0, WIDTH - 1)
PLAYER_START_Y = random.randint(0, HEIGHT - 1)

# World Constants
WORLD = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
BLOCK_ICON = "#"

# Place player in the world
WORLD[PLAYER_START_Y][PLAYER_START_X] = PLAYER_ICON

# Game Loop
while True:
    # Print the world
    for row in WORLD:
        print("".join(row))
    
    # Get player input
    move = input("Enter your move (w/a/s/d): ")
    
    # Clear the player's current position
    WORLD[PLAYER_START_Y][PLAYER_START_X] = " "
    
    # Update player position based on input
    if move == "w" and PLAYER_START_Y > 0:
        PLAYER_START_Y -= 1
    elif move == "s" and PLAYER_START_Y < HEIGHT - 1:
        PLAYER_START_Y += 1
    elif move == "a" and PLAYER_START_X > 0:
        PLAYER_START_X -= 1
    elif move == "d" and PLAYER_START_X < WIDTH - 1:
        PLAYER_START_X += 1
    
    # Place the player in the new position
    WORLD[PLAYER_START_Y][PLAYER_START_X] = PLAYER_ICON
