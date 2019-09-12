import pygame as game  # now instead of using pygame, you can use game

game.init()
windowScreen = game.display.set_mode((300, 300))
done = False

# Draw Rect as place where mouse pointer can be clicked
RectangularPlace = game.draw.rect(windowScreen, (255, 0, 0),
                                  (150, 150, 150, 150))
game.display.update()

# Main Loop
while not done:
    # Mouse position and button clicking.
    position = game.mouse.get_pos()
    leftPressed, rightPressed, centerPressed = game.mouse.get_pressed(
    )  # checking if left mouse button is collided with rect place or not
    if RectangularPlace.collidepoint(position) and leftPressed:
        print("You have clicked on a rectangle")
        # Quit pygame.
    for anyEvent in game.event.get():
        if anyEvent.type == game.QUIT:
            done = True
