import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))


walkRight = [pygame.image.load('Right1.png'), pygame.image.load('Right2.png'), pygame.image.load('Right3.png'),
             pygame.image.load('Right4.png'), pygame.image.load('Right5.png'), pygame.image.load('Right6.png'),
             pygame.image.load('Right7.png'), pygame.image.load('Right8.png'), pygame.image.load('Right9.png')]
walkLeft = [pygame.image.load('Left1.png'), pygame.image.load('Left2.png'), pygame.image.load('Left3.png'),
            pygame.image.load('Left4.png'), pygame.image.load('Left5.png'), pygame.image.load('Left6.png'),
            pygame.image.load('Left7.png'), pygame.image.load('Left8.png'), pygame.image.load('Left9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()


left = False
right = False
walkCount = 0


def Animation_Logic():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

   

    Animation_Logic()

pygame.quit()
