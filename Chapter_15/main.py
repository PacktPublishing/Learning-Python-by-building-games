import math
import time
import pygame
import pymunk
from characters import RoundBird
from level import Level


pygame.init()
screen = pygame.display.set_mode((1200, 650))
redbird = pygame.image.load(
    "../res/photos/red-bird3.png").convert_alpha()
background_image = pygame.image.load(
    "../res/photos/background3.png").convert_alpha()
sling_image = pygame.image.load(
    "../res/photos/sling-3.png").convert_alpha()
full_sprite = pygame.image.load(
    "../res/photos/full-sprite.png").convert_alpha()
rect_screen = pygame.Rect(181, 1050, 50, 50)
cropped_image = full_sprite.subsurface(rect_screen).copy()
pig_image = pygame.transform.scale(cropped_image, (30, 30)) #(30, 30) resulting height and width of pig

clock = pygame.time.Clock()


running = True

#base code
space_obj = pymunk.Space()
space_obj.gravity = (0.0, -700.0)

total_pig = []
total_birds = []
beams = []
columns = []
#color code
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)




mouse_distance = 0
rope_length = 90

angle = 0
mouse_x_pos = 0
mouse_y_pos = 0

mouse_pressed = False
time_of_release = 0

initial_x_sling, initial_y_sling = 135, 450
next_x_sling, next_y_sling = 160, 450



# Static floor
static_floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
static_lines_first = [pymunk.Segment(static_floor_body, (0.0, 060.0), (1200.0, 060.0), 0.0)]
static_lines_second = [pymunk.Segment(static_floor_body, (1200.0, 060.0), (1200.0, 800.0), 0.0)]

#lets add elasticity and friction to surface
for eachLine in static_lines_first:
    eachLine.elasticity = 0.95
    eachLine.friction = 1
    eachLine.collision_type = 3
    
for eachLine in static_lines_second:
    eachLine.elasticity = 0.95
    eachLine.friction = 1
    eachLine.collision_type = 3
space_obj.add(static_lines_first)


def convert_to_pygame(pos):
    """ pymunk to pygame coordinates"""
    return int(pos.x), int(-pos.y+600)


def vector(a, b):
    #return vector from points
    p = b[0] - a[0]
    q = b[1] - a[1]
    return (p, q)


def unit_vector(v):

    mag = ((v[0]**2)+(v[1]**2))**0.5
    if mag == 0:
        mag = 0.000000000000001
    unit_p = v[0] / mag
    unit_q = v[1] / mag
    return (unit_p, unit_q)


def distance(x0, y0, x1, y1):
    """distance between points"""
    dx = x1 - x0
    dy = y1 - y0
    dist = ((dx ** 2) + (dy ** 2)) ** 0.5
    return dist


def load_music():
    """Load the music"""
    song = '../res/sounds/angry-total_birds.ogg'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)


def sling_action():
    """Set up sling behavior"""
    global mouse_distance
    global rope_length
    global angle
    global mouse_x_pos
    global mouse_y_pos

    #add code inside sling function
    # Fixing bird to the sling rope
    vec = vector((initial_x_sling, initial_y_sling), (mouse_x_pos, mouse_y_pos))
    unit_vec = unit_vector(vec)
    uv_1 = unit_vec[0]
    uv_2 = unit_vec[1]
    mouse_distance = distance(initial_x_sling, initial_y_sling, mouse_x_pos, mouse_y_pos) #point at which currrent bird id
    fix_pos = (uv_1*rope_length+initial_x_sling, uv_2*rope_length+initial_y_sling)
    highest_length = 102 #when stretched

    #to make bird stay within rope
    x_redbird = mouse_x_pos - 20
    y_redbird = mouse_y_pos - 20
    if mouse_distance > rope_length:
        pux, puy = fix_pos
        pux -= 20
        puy -= 20
        first_pos = pux, puy
        screen.blit(redbird, first_pos)
        second_pos = (uv_1*highest_length+initial_x_sling, uv_2*highest_length+initial_y_sling) #current position
        pygame.draw.line(screen, (255, 0, 0), (next_x_sling, next_y_sling), second_pos, 5) #catapult rope
        screen.blit(redbird, first_pos)
        pygame.draw.line(screen, (255, 0, 0), (initial_x_sling, initial_y_sling), second_pos, 5) #ANOTHER SIDE of catapult
    else:
        #when not fully stretched
        mouse_distance += 10
        third_pos = (uv_1*mouse_distance+initial_x_sling, uv_2*mouse_distance+initial_y_sling)
        pygame.draw.line(screen, (0, 0, 0), (next_x_sling, next_y_sling), third_pos, 5)
        screen.blit(redbird, (x_redbird, y_redbird))
        pygame.draw.line(screen, (0, 0, 0), (initial_x_sling, initial_y_sling), third_pos, 5)
    # Angle of impulse

    change_in_y = mouse_y_pos - initial_y_sling
    change_in_x = mouse_x_pos - initial_x_sling
    if change_in_x == 0:
        dx = 0.00000000000001
    angle = math.atan((float(change_in_y))/change_in_x)


""" collision handler post solve methods"""

def post_solve_bird_pig(arbiter, space_obj, _):
    """Action to perform after collision between bird and pig"""

    object1, object2 = arbiter.shapes #Arbiter class obj
    bird_body = object1.body
    pig_body = object2.body
    bird_position = convert_to_pygame(bird_body.position)
    pig_position = convert_to_pygame(pig_body.position)
    radius = 30
    pygame.draw.circle(screen, (255, 0, 0), bird_position, radius, 4)  #screen => pygame surface
    pygame.draw.circle(screen, RED, pig_position, radius, 4)
    #removal of pig
    removed_pigs_after_sling = []
    for pig in total_pig:
        if pig_body == pig.body:
            pig.life -= 20 #decrease life
            removed_pigs_after_sling.append(pig)

    for eachPig in removed_pigs_after_sling:
        space_obj.remove(eachPig.shape, eachPig.shape.body)
        total_pig.remove(eachPig)


def post_solve_bird_wood(arbiter, space_obj, _):
    """Action to perform after collision between bird and wood structure"""
    #removing polygon
    removed_poly = []
    if arbiter.total_impulse.length > 1100:
        object1, object2 = arbiter.shapes
        for Each_column in columns:
            if object2 == Each_column.shape:
                removed_poly.append(Each_column)
        for Each_beam in beams:
            if object2 == Each_beam.shape:
                removed_poly.append(Each_beam)
        for Each_poly in removed_poly:
            if Each_poly in columns:
                columns.remove(Each_poly)
            if Each_poly in beams:
                beams.remove(Each_poly)
        space_obj.remove(object2, object2.body)
        #you can also remove bird if you want


def post_solve_pig_wood(arbiter, space_obj, _):
    """Action to perform after collision between pig and wood"""
    removed_pigs = []
    if arbiter.total_impulse.length > 700:
        pig_shape, wood_shape = arbiter.shapes
        for pig in total_pig:
            if pig_shape == pig.shape:
                pig.life -= 20

                if pig.life <= 0: #when life is 0
                    removed_pigs.append(pig)
    for Each_pig in removed_pigs:
        space_obj.remove(Each_pig.shape, Each_pig.shape.body)
        total_pig.remove(Each_pig)


# bird and total_pig
space_obj.add_collision_handler(0, 1).post_solve=post_solve_bird_pig
# bird and wood
space_obj.add_collision_handler(0, 2).post_solve=post_solve_bird_wood
# pig and wood
space_obj.add_collision_handler(1, 2).post_solve=post_solve_pig_wood
#load_music()
level = Level(total_pig, columns, beams, space_obj)
level.number = 0
level.load_level()

while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if (pygame.mouse.get_pressed()[0] and mouse_x_pos > 100 and
                mouse_x_pos < 250 and mouse_y_pos > 370 and mouse_y_pos < 550):
            mouse_pressed = True
        if (event.type == pygame.MOUSEBUTTONUP and
                event.button == 1 and mouse_pressed):
            # Release new bird
            mouse_pressed = False
            if level.number_of_birds > 0:
                level.number_of_birds -= 1
                time_of_release = time.time()*1000
                x_initial = 154
                y_initial = 156


                if mouse_distance > rope_length:
                    mouse_distance = rope_length
                if mouse_x_pos < initial_x_sling+5:
                    bird = RoundBird(mouse_distance, angle, x_initial, y_initial, space_obj)
                    total_birds.append(bird)
                else:
                    bird = RoundBird(-mouse_distance, angle, x_initial, y_initial, space_obj)
                    total_birds.append(bird)
                if level.number_of_birds == 0:
                    game_finish_time = time.time()

    mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
    # Draw background
    screen.fill((130, 200, 100))
    screen.blit(background_image, (0, -50))
    # Draw first part of the sling
    rect = pygame.Rect(50, 0, 70, 220)
    screen.blit(sling_image, (138, 420), rect)
    # Draw the trail left behind

    if level.number_of_birds > 0:
        for i in range(level.number_of_birds-1):
            x = 100 - (i*35)
            screen.blit(redbird, (x, 508))


    # Draw sling behavior
    if mouse_pressed and level.number_of_birds > 0:
        sling_action()
    else: #blit bird when no stretch
        if time.time()*1000 - time_of_release > 300 and level.number_of_birds > 0:
            screen.blit(redbird, (130, 426))

    removed_bird_after_sling = []
    removed_pigs_after_sling = []
    #counter += 1
    # Draw total_birds
    for bird in total_birds:
        if bird.shape.body.position.y < 0:
            removed_bird_after_sling.append(bird)
        p = convert_to_pygame(bird.shape.body.position)
        x, y = p
        x -= 22
        y -= 20
        screen.blit(redbird, (x, y))
        pygame.draw.circle(screen, BLUE,
                           p, int(bird.shape.radius), 2)


    # Remove total_birds and total_pig
    for bird in removed_bird_after_sling:
        space_obj.remove(bird.shape, bird.shape.body)
        total_birds.remove(bird)
    for pig in removed_pigs_after_sling:
        space_obj.remove(pig.shape, pig.shape.body)
        total_pig.remove(pig)


    #life = 0
    # Draw total_pig
    for Each_pig in total_pig:

        pig = Each_pig.shape
        if pig.body.position.y < 0:
            removed_pigs_after_sling.append(pig)

        pos = convert_to_pygame(pig.body.position) #pos is tuple
        x_pos, y_pos = pos

        angle_degrees = math.degrees(pig.body.angle)

        pig_rotated_img = pygame.transform.rotate(pig_image, angle_degrees) #small random rotation within wooden frame
        width,height = pig_rotated_img.get_size()
        x_pos -= width*0.5
        y_pos -= height*0.5
        screen.blit(pig_rotated_img, (x_pos, y_pos))
        pygame.draw.circle(screen, BLUE, pos, int(pig.radius), 2)


    # Draw columns and Beams
    for column in columns:
        column.draw_poly('columns', screen)
    for beam in beams:
        beam.draw_poly('beams', screen)


    # Update simulation
    """ check URL:http://www.pymunk.org/en/latest/_modules/pymunk/space.html """

    time_step_change = 1.0/50.0/2.
    for x in range(2):
        space_obj.step(time_step_change) # make two updates per frame for better stability
    # Drawing second part of the sling
    rect_for_sling = pygame.Rect(0, 0, 60, 200)
    screen.blit(sling_image, (120, 420), rect_for_sling)


    pygame.display.flip()
    clock.tick(50)

