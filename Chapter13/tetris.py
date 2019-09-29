import pygame
import random

pygame.font.init()

# GLOBALS VARS
width = 800
height = 700
game_width = 300  # meaning 300 // 10 = 30 width per block
game_height = 600  # meaning 600 // 20 = 30 height per block
shape_size = 30

top_left_x = (width - game_width) // 2
top_left_y = height - game_height


# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

game_objects = [S, Z, I, O, J, L, T]
objects_color = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Shape(object):  # *
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = objects_color[game_objects.index(shape)]
        self.rotation = 0


def build_Grid(occupied={}):  # *
    shapes_grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for row in range(len(shapes_grid)):
        for column in range(len(shapes_grid[row])):
            if (column, row) in occupied:
                piece = occupied[(column,row)]
                shapes_grid[row][column] = piece
    return shapes_grid


def define_shape_position(shape_piece):
    positions = []
    list_of_shapes = shape_piece.shape[shape_piece.rotation % len(shape_piece.shape)]

    for i, line in enumerate(list_of_shapes):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape_piece.x + j, shape_piece.y + i))

    for p, block_pos in enumerate(positions):
        positions[p] = (block_pos[0] - 2, block_pos[1] - 4)

    return positions


def check_Moves(shape, grid):
    valid_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    valid_pos = [j for sub in valid_pos for j in sub]

    shape_pos = define_shape_position(shape)

    for eachPos in shape_pos:
        if eachPos not in valid_pos:
            if eachPos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False


def generate_Shapes():
    return Shape(5, 0, random.choice(game_objects))


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + game_width /2 - (label.get_width()/2), top_left_y + game_height/2 - label.get_height()/2))


def show_grid(screen_surface, grid):
    side_x = top_left_x
    side_y = top_left_y

    for eachRow in range(len(grid)):
        pygame.draw.line(screen_surface, (128,128,128), (side_x, side_y + eachRow*shape_size), (side_x+game_width, side_y+ eachRow*shape_size))
        for eachCol in range(len(grid[eachRow])):
            pygame.draw.line(screen_surface, (128, 128, 128), (side_x + eachCol*shape_size, side_y),(side_x + eachCol*shape_size, side_y + game_height))


def delete_Row(grid, occupied):

    black_background_color = (0, 0, 0)
    number_of_rows_deleted = 0
    for i in range(len(grid)-1, -1, -1):
        eachRow = grid[i]
        if black_background_color not in eachRow:
            number_of_rows_deleted += 1
            index_of_deleted_rows = i
            for j in range(len(eachRow)):
                try:
                    del occupied[(j,i)]
                except:
                    continue

    if number_of_rows_deleted > 0:
        for position in sorted(list(occupied), key=lambda x: x[1])[::-1]:
            x, y = position
            if y < index_of_deleted_rows:
                newPos = (x, y + number_of_rows_deleted)
                occupied[newPos] = occupied.pop(position)

    return number_of_rows_deleted


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    sx = top_left_x + game_width + 50
    sy = top_left_y + game_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*shape_size, sy + i*shape_size, shape_size, shape_size), 0)

    surface.blit(label, (sx + 10, sy - 30))


def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))


def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score


def create_Grid(screen_surface, grid_scene, score=0, last_score = 0):
    screen_surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    screen_surface.blit(label, (top_left_x + game_width / 2 - (label.get_width() / 2), 30))

    """ current score and last score are modifications to the game
    
    -----------------------------------------------------------------
     
     """
    # current score
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), 1, (255,255,255))


    sx = top_left_x + game_width + 50
    sy = top_left_y + game_height/2 - 100

    screen_surface.blit(label, (sx + 20, sy + 160))
    # last score
    label = font.render('High Score: ' + last_score, 1, (255,255,255))

    sx = top_left_x - 200
    sy = top_left_y + 200

    screen_surface.blit(label, (sx + 20, sy + 160))

    for i in range(len(grid_scene)):
        for j in range(len(grid_scene[i])):
            pygame.draw.rect(screen_surface, grid_scene[i][j], (top_left_x + j*shape_size, top_left_y + i*shape_size, shape_size, shape_size), 0)

    pygame.draw.rect(screen_surface, (255, 0, 0), (top_left_x, top_left_y, game_width, game_height), 5)

    show_grid(screen_surface, grid_scene)
    #pygame.display.update()


def main(win):  # *

    last_score = max_score()
    occupied = {}
    grid = build_Grid(occupied)

    change_shape = False
    done  = False
    current_shape = generate_Shapes()
    next_shape = generate_Shapes()
    clock = pygame.time.Clock()

    timeforFall = 0
    speedforFall = 0.27
    level_time = 0
    score = 0

    while not done:
        grid = build_Grid(occupied)
        timeforFall += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if timeforFall/1000 > speedforFall:
            timeforFall = 0
            current_shape.y += 1
            if not(check_Moves(current_shape, grid)) and current_shape.y > 0:
                current_shape.y -= 1
                change_shape = True

        for eachEvent in pygame.event.get():
            if eachEvent.type == pygame.QUIT:
                done = True
                pygame.display.quit()

            if eachEvent.type == pygame.KEYDOWN:
                if eachEvent.key == pygame.K_LEFT:
                    current_shape.x -= 1
                    if not(check_Moves(current_shape, grid)):
                        current_shape.x += 1
                if eachEvent.key == pygame.K_RIGHT:
                    current_shape.x += 1
                    if not(check_Moves(current_shape, grid)):
                        current_shape.x -= 1
                if eachEvent.key == pygame.K_DOWN:
                    current_shape.y += 1
                    if not(check_Moves(current_shape, grid)):
                        current_shape.y -= 1
                if eachEvent.key == pygame.K_UP:
                    current_shape.rotation += 1
                    if not(check_Moves(current_shape, grid)):
                        current_shape.rotation -= 1

        position_of_shape = define_shape_position(current_shape)

        for i in range(len(position_of_shape)):
            x, y = position_of_shape[i]
            if y > -1:
                grid[y][x] = current_shape.color

        """will change piece """
        if change_shape:
            for eachPos in position_of_shape:
                pos = (eachPos[0], eachPos[1])
                occupied[pos] = current_shape.color
            current_shape = next_shape
            next_shape = generate_Shapes()
            change_shape = False
            score += delete_Row(grid, occupied) * 10

        create_Grid(win, grid, score, last_score)
        draw_next_shape(next_shape, win)
        pygame.display.update()

        """ optional check: whether lost or not"""
        if check_lost(occupied):
            draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)


def Welcome_Screen(surface):  # *
    done = False
    while not done:
        surface.fill((128,0, 128))
        draw_text_middle(win, 'Press Any Key To Play Tetris!!', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                main(surface)

    pygame.display.quit()


win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tetris')
Welcome_Screen(win)
