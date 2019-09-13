import pygame
import random

# Initialize the pygame
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# Set the height and width of the screen
SIZE = [500, 500]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")

# Create an empty list to store position of snow
snowArray = []

# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x_pos = random.randrange(0, 500)
    y_pos = random.randrange(0, 500)
    snowArray.append([x_pos, y_pos])

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
finish = False
while not finish:

    for anyEvent in pygame.event.get():  # User did something
        if anyEvent.type == pygame.QUIT:  # If user clicked close
            finish = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Process each snow flake in the list
    for i in range(len(snowArray)):

        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snowArray[i], 2)

        # Move the snow flake down one pixel
        snowArray[i][1] += 1

        # If the snow flake has moved off the bottom of the screen
        if snowArray[i][1] > 500:
            # Reset it just above the top
            y_pos = random.randrange(-40, -10)
            snowArray[i][1] = y_pos
            # Give it a new x position
            x_pos = random.randrange(0, 500)
            snowArray[i][0] = x_pos

    # Update screen with what you've drawn.
    pygame.display.update()
    clock.tick(20)

# if you remove following line of code, IDLE will hang at exit
pygame.quit()
