# Conway's Game of Life!

import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
MARGIN = 1

# The size of the grid
SIZE = 50

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(SIZE):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(SIZE):
        grid[row].append(0)  # Append a cell

# Fill in the grid with random values
for row in range(SIZE):
    for column in range(SIZE):
        grid[row][column] = random.randint(0, 1)

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [510, 510]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    # Draw the grid
    for row in range(SIZE):
        for column in range(SIZE):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

    # --- Game logic should go here
    new_grid = []
    for row in range(SIZE):
        # Add an empty array that will hold each cell
        # in this row
        new_grid.append([])
        for column in range(SIZE):
            new_grid[row].append(0)

    for row in range(SIZE):
        for column in range(SIZE):
            # Count the number of neighbors
            neighbors = 0
            # Find the number of neighbors of the current cell
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        neighbors += grid[row + i][column + j]
                    except IndexError:
                        pass
            if grid[row][column] == 1:
                neighbors -= 1
            if grid[row][column] == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[row][column] = 1
            if grid[row][column] == 0 and neighbors == 3:
                new_grid[row][column] = 1

    grid = new_grid
    time.sleep(.1)

# Close the window and quit.
pygame.quit()

