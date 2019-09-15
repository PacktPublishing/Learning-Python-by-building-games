import pygame
import random

pygame.font.init()

# declare GLOBALS
width = 800
height = 700
game_width = 300  # meaning 300 // 10 = 30 width per block
game_height = 600  # meaning 600 // 20 = 30 height per block
shape_size = 30

top_left_x = (width - game_width) // 2
top_left_y = height - game_height

# SHAPE FORMATS

S = [['.....', '.....', '..00.', '.00..', '.....'],
     ['.....', '..0..', '..00.', '...0.', '.....']]

Z = [['.....', '.....', '.00..', '..00.', '.....'],
     ['.....', '..0..', '.00..', '.0...', '.....']]

I = [['..0..', '..0..', '..0..', '..0..', '.....'],
     ['.....', '0000.', '.....', '.....', '.....']]

O = [['.....', '.....', '.00..', '.00..', '.....']]

J = [['.....', '.0...', '.000.', '.....', '.....'],
     ['.....', '..00.', '..0..', '..0..', '.....'],
     ['.....', '.....', '.000.', '...0.', '.....'],
     ['.....', '..0..', '..0..', '.00..', '.....']]

L = [['.....', '...0.', '.000.', '.....', '.....'],
     ['.....', '..0..', '..0..', '..00.', '.....'],
     ['.....', '.....', '.000.', '.0...', '.....'],
     ['.....', '.00..', '..0..', '..0..', '.....']]

T = [['.....', '..0..', '.000.', '.....', '.....'],
     ['.....', '..0..', '..00.', '..0..', '.....'],
     ['.....', '.....', '.000.', '..0..', '.....'],
     ['.....', '..0..', '.00..', '..0..', '.....']]

game_objects = [S, Z, I, O, J, L, T]
objects_color = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0),
                 (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Shape(object):  # *
    def __init__(self, column, row, shape):
        self.dim_x = column
        self.dim_y = row
        self.shape = shape
        self.color = objects_color[game_objects.index(shape)]
        self.rotation = 0


def build_grid(occupied={}):  # *
    shapes_grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for row in range(len(shapes_grid)):
        for column in range(len(shapes_grid[row])):
            if (column, row) in occupied:
                piece = occupied[(column, row)]
                shapes_grid[row][column] = piece
    return shapes_grid


def define_shape_position(shape_piece):
    positions = []
    list_of_shapes = shape_piece.shape[shape_piece.rotation %
                                       len(shape_piece.shape)]

    for i, row in enumerate(list_of_shapes):
        row = list(row)
        for j, column in enumerate(row):
            if column == '0':
                positions.append(
                    (shape_piece.dim_x + j, shape_piece.dim_y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def check_moves(shape, grid):
    valid_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)]
                 for i in range(20)]
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


def generate_shapes():
    return Shape(5, 0, random.choice(game_objects))


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label,
                 (top_left_x + game_width / 2 - (label.get_width() / 2),
                  top_left_y + game_height / 2 - label.get_height() / 2))


def show_grid(surface, grid):
    side_x = top_left_x
    side_y = top_left_y

    for eachRow in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128),
                         (side_x, side_y + eachRow * shape_size),
                         (side_x + game_width, side_y + eachRow * shape_size))
        for eachCol in range(len(grid[eachRow])):
            pygame.draw.line(
                surface, (128, 128, 128),
                (side_x + eachCol * shape_size, side_y),
                (side_x + eachCol * shape_size, side_y + game_height))


def delete_row(grid, occupied):

    black_background_color = (0, 0, 0)
    number_of_rows_deleted = 0
    for i in range(len(grid) - 1, -1, -1):
        eachRow = grid[i]
        if black_background_color not in eachRow:
            number_of_rows_deleted += 1
            ind = i
            for j in range(len(eachRow)):
                try:
                    del occupied[(j, i)]
                except:
                    continue

    if number_of_rows_deleted > 0:
        for key in sorted(list(occupied), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + number_of_rows_deleted)
                occupied[newKey] = occupied.pop(key)

    return number_of_rows_deleted


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = top_left_x + game_width + 50
    sy = top_left_y + game_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color,
                                 (sx + j * shape_size, sy + i * shape_size,
                                  shape_size, shape_size), 0)

    surface.blit(label, (sx + 10, sy - 30))


def draw_window(surface, grid, score=0):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label,
                 (top_left_x + game_width / 2 - (label.get_width() / 2), 30))

    # current score
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), 1, (255, 255, 255))

    sx = top_left_x + game_width + 50
    sy = top_left_y + game_height / 2 - 100

    surface.blit(label, (sx + 20, sy + 160))

    sx = top_left_x - 200
    sy = top_left_y + 200

    surface.blit(label, (sx + 20, sy + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j * shape_size, top_left_y +
                              i * shape_size, shape_size, shape_size), 0)

    pygame.draw.rect(surface, (255, 0, 0),
                     (top_left_x, top_left_y, game_width, game_height), 5)

    show_grid(surface, grid)
    # pygame.display.update()


def main(win):  # *
    locked_positions = {}
    grid = build_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = generate_shapes()
    next_piece = generate_shapes()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = build_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.dim_y += 1
            if not (check_moves(current_piece,
                                grid)) and current_piece.dim_y > 0:
                current_piece.dim_y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.dim_x -= 1
                    if not (check_moves(current_piece, grid)):
                        current_piece.dim_x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.dim_x += 1
                    if not (check_moves(current_piece, grid)):
                        current_piece.dim_x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.dim_y += 1
                    if not (check_moves(current_piece, grid)):
                        current_piece.dim_y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (check_moves(current_piece, grid)):
                        current_piece.rotation -= 1

        shape_pos = define_shape_position(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = generate_shapes()
            change_piece = False
            score += delete_row(grid, locked_positions) * 10

        draw_window(win, grid, score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 80, (255, 255, 255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False


def welcome_screen(surface):  # *
    run = True
    while run:
        surface.fill((128, 0, 128))
        draw_text_middle(surface, 'Press ANY Key To Play Tetris', 60,
                         (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(surface)

    pygame.display.quit()


win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tetris')

welcome_screen(win)
