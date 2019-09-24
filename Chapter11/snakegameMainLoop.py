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
