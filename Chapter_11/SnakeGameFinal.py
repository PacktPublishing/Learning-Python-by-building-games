import pygame as game
import time
import random

game.init()

color_white = (255,255,255)
color_black = (0,0,0)
color_red = (255,0,0)


display_width = 800
display_height  = 600

DisplayScreen = game.display.set_mode((display_width,display_height))
game.display.set_caption(''")

image = game.image.load('snakehead.png')
appleimg = game.image.load('apple.png')

objectClock = game.time.objectClock()

Width_Apple = 30
pixel_size = 10 #box size
FPS = 15

arrow_key = "right"

font_small = game.font.SysFont("comicsansms", 25)
font_medium = game.font.SysFont("comicsansms", 50)
font_large = game.font.SysFont("comicsansms", 80)


def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    DisplayScreen.blit(text, [0,0])

def randAppleGen():
    XpositionApple = round(random.randrange(0, display_width-Width_Apple))
    YpositionApple = round(random.randrange(0, display_height-Width_Apple))

    return XpositionApple,YpositionApple



def intro_for_game():

    intro_screen = True

    while intro_screen:

        for eachEvent in game.event.get():
            if eachEvent.type == game.QUIT:
                game.quit()
                quit()

            if eachEvent.type == game.KEYDOWN:
                if eachEvent.key == game.K_c:
                    intro_screen = False
                if eachEvent.key == game.K_q:
                    game.quit()
                    quit()
   
        DisplayScreen.fill(color_white)
        display_ScreenMessage("Welcome to Snake",
                          color_green,
                          -99,
                          "large")
     
    

        display_ScreenMessage("Made by Python Programmer!",
                          black,
                          50)

        display_ScreenMessage("Press C to play or Q to quit.",
                          black,
                          180)
    
        game.display.update()
        objectClock.tick(15)
        
        


def drawSnake(pixel_size, snakeArray):

    if arrow_key == "right":
        head_of_Snake = game.transform.rotate(image, 270)

    if arrow_key == "left":
        head_of_Snake = game.transform.rotate(image, 90)

    if arrow_key == "up":
        head_of_Snake = image

    if arrow_key == "down":
        head_of_Snake = game.transform.rotate(image, 180)
        
    
    DisplayScreen.blit(image, (snakeArray[-1][0], snakeArray[-1][1]))
    
    for eachSegment in snakeArray[:-1]:
        game.draw.rect(DisplayScreen, color_green, [eachSegment[0],eachSegment[1],pixel_size,pixel_size])

def objects_text(sample_text,sample_color,sample_size):
    if sample_size == "small":
        surface_for_text = font_small.render(sample_text, True, sample_color)
    elif sample_size == "medium":
        surface_for_text = font_medium.render(sample_text, True, sample_color)
    elif sample_size == "large":
        surface_for_text = font_large.render(sample_text, True, sample_color)

    
    return surface_for_text, surface_for_text.get_rect()
    
    
def display_ScreenMessage(message,font_color, yDisplace=0, font_size = "small"):
    textSurface, textRectShape = objects_text(message,font_color, font_size)
    textRectShape.center = (display_width / 2), (display_height / 2)+yDisplace
    DisplayScreen.blit(textSurface, textRectShape)


def MainLoopForGame():
    global arrow_key

    arrow_key = 'right'
    gameOver = False
    gameFinish = False

    change_x = display_width/2
    change_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeArray = []
    snakeLength = 1

    XpositionApple,YpositionApple = randAppleGen()
    
    while not gameOver:

        while gameFinish == True:
            DisplayScreen.fill(color_white)
            
            game.display.update()

            for anyEvent in game.anyEvent.get():
                    
                if anyEvent.type == game.KEYDOWN:
                    if anyEvent.key == game.K_q:
                        gameOver = True
                        gameFinish = False
                    if anyEvent.key == game.K_c:
                        MainLoopForGame()

        
        for anyEvent in game.anyEvent.get():
            if anyEvent.type == game.QUIT:
                gameOver = True
            if anyEvent.type == game.KEYDOWN:
                if anyEvent.key == game.K_LEFT:
                    arrow_key = "left"
                    lead_x_change = -pixel_size
                    lead_y_change = 0
                elif anyEvent.key == game.K_RIGHT:
                    arrow_key = "right"
                    lead_x_change = pixel_size
                    lead_y_change = 0
                elif anyEvent.key == game.K_UP:
                    arrow_key = "up"
                    lead_y_change = -pixel_size
                    lead_x_change = 0
                elif anyEvent.key == game.K_DOWN:
                    arrow_key = "down"
                    lead_y_change = pixel_size
                    lead_x_change = 0

        if change_x >= display_width or change_x < 0 or change_y >= display_height or change_y < 0:
            gameFinish = True
      

        change_x += lead_x_change
        change_y += lead_y_change
        
        DisplayScreen.fill(color_white)
  """
Code before making snake head image

 game.draw.rect(DisplayScreen, color_red, [XpositionApple, YpositionApple, Width_Apple, Width_Apple])
        game.draw.rect(DisplayScreen, color_black, [change_x,change_y,pixel_size, pixel_size])
        game.display.update()

        objectClock.tick(FPS)
        
    game.quit()
    quit()

MainLoopForGame()



"""

        DisplayScreen.blit(appleimg, (XpositionApple, YpositionApple))


        head_of_Snake = []
        head_of_Snake.append(change_x)
        head_of_Snake.append(change_y)
        snakeArray.append(head_of_Snake)

        if len(snakeArray) > snakeLength:
            del snakeArray[0]

        for eachPart in snakeArray[:-1]:
            if eachPart == head_of_Snake:
                gameFinish = True

        
        drawSnake(pixel_size, snakeArray)

        score(snakeLength-1)

        
        game.display.update()

        if change_x > XpositionApple and change_x < XpositionApple + Width_Apple or change_x + pixel_size > XpositionApple and change_x + pixel_size < XpositionApple + Width_Apple:

            if change_y > YpositionApple and change_y < YpositionApple + Width_Apple:

                XpositionApple,YpositionApple = randAppleGen()
                snakeLength += 1

            elif change_y + pixel_size > YpositionApple and change_y + pixel_size < YpositionApple + Width_Apple:

                XpositionApple,YpositionApple = randAppleGen()
                snakeLength += 1

            
            
        objectClock.tick(FPS)
        
    game.quit()
    quit()

intro_for_game()
MainLoopForGame()















