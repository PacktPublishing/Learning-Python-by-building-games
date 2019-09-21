import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *


Frame_Rate = 60
ANIMATION_SPEED = 0.18  # pixels per millisecond
WINDOW_WIDTH = 284 * 2     # BG image size: 284x512 px; tiled twice
WINDOW_HEIGHT = 512


class Bird(pygame.sprite.Sprite):
    """Represents the bird controlled by the player.

    The bird is the 'hero' of this game.  The player can make it climb
    (ascend quickly), otherwise it sinks (descends more slowly).  It must
    pass through the space in between pipes (for every pipe passed, one
    point is scored); if it crashes into a pipe, the game ends.

    Attributes:
    x: The bird's X coordinate.
    y: The bird's Y coordinate.
    msec_to_climb: The number of milliseconds left to climb, where a
        complete climb lasts Bird.CLIMB_DURATION milliseconds.

    Constants:
    WIDTH: The width, in pixels, of the bird's image.
    HEIGHT: The height, in pixels, of the bird's image.
    SINK_SPEED: With which speed, in pixels per millisecond, the bird
        descends in one second while not climbing.
    CLIMB_SPEED: With which speed, in pixels per millisecond, the bird
        ascends in one second while climbing, on average.  See also the
        Bird.update docstring.
    CLIMB_DURATION: The number of milliseconds it takes the bird to
        execute a complete climb.
    """

    WIDTH = HEIGHT = 30
    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3

    def __init__(self, x, y, msec_to_climb, images):
        """Initialise a new Bird instance.

        Arguments:
        x: The bird's initial X coordinate.
        y: The bird's initial Y coordinate.
        msec_to_climb: The number of milliseconds left to climb, where a
            complete climb lasts Bird.CLIMB_DURATION milliseconds.  Use
            this if you want the bird to make a (small?) climb at the
            very beginning of the game.
        images: A tuple containing the images used by this bird.  It
            must contain the following images, in the following order:
                0. image of the bird with its wing pointing upward
                1. image of the bird with its wing pointing downward
        """
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)

    def update(self, delta_frames=1):
        """Update the bird's position.

        This function uses the cosine function to achieve a smooth climb:
        In the first and last few frames, the bird climbs very little, in the
        middle of the climb, it climbs a lot.
        One complete climb lasts CLIMB_DURATION milliseconds, during which
        the bird ascends with an average speed of CLIMB_SPEED px/ms.
        This Bird's msec_to_climb attribute will automatically be
        decreased accordingly if it was > 0 when this method was called.

        Arguments:
        delta_frames: The number of frames elapsed since this method was
            last called.
        """
        if self.msec_to_climb > 0:
            frac_climb_done = 1 - self.msec_to_climb/Bird.CLIMB_DURATION
            self.y -= (Bird.CLIMB_SPEED * frames_to_msec(delta_frames) *
                       (1 - math.cos(frac_climb_done * math.pi)))
            self.msec_to_climb -= frames_to_msec(delta_frames)
        else:
            self.y += Bird.SINK_SPEED * frames_to_msec(delta_frames)

    @property
    def image(self):
        """Get a Surface containing this bird's image.

        This will decide whether to return an image where the bird's
        visible wing is pointing upward or where it is pointing downward
        based on pygame.time.get_ticks().  This will animate the flapping
        bird, even though pygame doesn't support animated GIFs.
        """
        if pygame.time.get_ticks() % 500 >= 250:
            return self._img_wingup
        else:
            return self._img_wingdown

    @property
    def mask(self):
        """Get a bitmask for use in collision detection.

        The bitmask excludes all pixels in self.image with a
        transparency greater than 127."""
        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return self._mask_wingdown

    @property
    def rect(self):
        """Get the bird's position, width, and height, as a pygame.Rect."""
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)


class PipePair(pygame.sprite.Sprite):
    """Represents an obstacle.

    A PipePair has a top and a bottom pipe, and only between them can
    the bird pass -- if it collides with either part, the game is over.

    Attributes:
    x: The PipePair's X position.  This is a float, to make movement
        smoother.  Note that there is no y attribute, as it will only
        ever be 0.
    image: A pygame.Surface which can be blitted to the display surface
        to display the PipePair.
    mask: A bitmask which excludes all pixels in self.image with a
        transparency greater than 127.  This can be used for collision
        detection.
    top_pipe_pieces: The number of pieces, including the end piece, in the
        top pipe.
    bottom_pipe_pieces: The number of pieces, including the end piece, in
        the bottom pipe.

    Constants:
    WIDTH: The width, in pixels, of a pipe piece.  Because a pipe is
        only one piece wide, this is also the width of a PipePair's
        image.
    HEIGHT_PIECE: The height, in pixels, of a pipe piece.
    ADD_INTERVAL: The interval, in milliseconds, in between adding new
        pipes.
    """

    WIDTH = 80
    HEIGHT_PIECE = 32
    ADD_INTERVAL = 3000

    def __init__(self, end_image_pipe, body_image_pipe):
        """Initialises a new random PipePair.

        The new PipePair will automatically be assigned an x attribute of
        float(WINDOW_WIDTH - 1).

        Arguments:
        end_image_pipe: The image to use to represent a pipe's end piece.
        body_image_pipe: The image to use to represent one horizontal slice
            of a pipe's body.
        """
        self.x = float(WINDOW_WIDTH - 1)
        self.score_counted = False

        self.image = pygame.Surface((PipePair.WIDTH, WINDOW_HEIGHT), SRCALPHA)
        self.image.convert()   # speeds up blitting
        self.image.fill((0, 0, 0, 0))
        total_pipe_body_pieces = int(
            (WINDOW_HEIGHT -                  # fill window from top to bottom
             3 * Bird.HEIGHT -             # make room for bird to fit through
             3 * PipePair.HEIGHT_PIECE) /  # 2 end pieces + 1 body piece
            PipePair.HEIGHT_PIECE          # to get number of pipe pieces
        )
        self.bottom_pipe_pieces = randint(1, total_pipe_body_pieces)
        self.top_pipe_pieces = total_pipe_body_pieces - self.bottom_pipe_pieces

        # bottom pipe
        for i in range(1, self.bottom_pipe_pieces + 1):
            piece_pos = (0, WINDOW_HEIGHT - i*PipePair.HEIGHT_PIECE)
            self.image.blit(body_image_pipe, piece_pos)
        bottom_pipe_end_y = WINDOW_HEIGHT - self.height_bottomPipe_px
        bottom_end_piece_pos = (0, bottom_pipe_end_y - PipePair.HEIGHT_PIECE)
        self.image.blit(end_image_pipe, bottom_end_piece_pos)

        # top pipe
        for i in range(self.top_pipe_pieces):
            self.image.blit(body_image_pipe, (0, i * PipePair.HEIGHT_PIECE))
        top_pipe_end_y = self.height_topPipe_px
        self.image.blit(end_image_pipe, (0, top_pipe_end_y))

        # compensate for added end pieces
        self.top_pipe_pieces += 1
        self.bottom_pipe_pieces += 1

        # for collision detection
        self.mask = pygame.mask.from_surface(self.image)

    @property
    def height_topPipe_px(self):
        """Get the top pipe's height, in pixels."""
        return self.top_pipe_pieces * PipePair.HEIGHT_PIECE

    @property
    def height_bottomPipe_px(self):
        """Get the bottom pipe's height, in pixels."""
        return self.bottom_pipe_pieces * PipePair.HEIGHT_PIECE

    @property
    def visible(self):
        """Get whether this PipePair on screen, visible to the player."""
        return -PipePair.WIDTH < self.x < WINDOW_WIDTH

    @property
    def rect(self):
        """Get the Rect which contains this PipePair."""
        return Rect(self.x, 0, PipePair.WIDTH, PipePair.HEIGHT_PIECE)

    def update(self, delta_frames=1):
        """Update the PipePair's position.

        Arguments:
        delta_frames: The number of frames elapsed since this method was
            last called.
        """
        self.x -= ANIMATION_SPEED * frames_to_msec(delta_frames)

    def collides_with(self, bird):
        """Get whether the bird collides with a pipe in this PipePair.

        Arguments:
        bird: The Bird which should be tested for collision with this
            PipePair.
        """
        return pygame.sprite.collide_mask(self, bird)


def loading_Images():
    """Load all images required by the game and return a dict of them.

    The returned dict has the following keys:
    game_background: The game's game_background image.
    WingUp: An image of the bird with its wing pointing upward.
        Use this and WingDown to create a flapping bird.
    WingDown: An image of the bird with its wing pointing downward.
        Use this and WingUp to create a flapping bird.
    endPipe: An image of a pipe's end piece (the slightly wider bit).
        Use this and bodyPipe to make pipes.
    bodyPipe: An image of a slice of a pipe's body.  Use this and
        bodyPipe to make pipes.
    """

    def loading_Image(img_file_name):
        """Return the loaded pygame image with the specified file name.

        This function looks for images in the game's images folder
        (./images/).  All images are converted before being returned to
        speed up blitting.

        Arguments:
        img_file_name: The file name (including its extension, e.g.
            '.png') of the required image, without a file path.
        """
        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'game_background': loading_Image('background.png'),
            'endPipe': loading_Image('pipe_end.png'),
            'bodyPipe': loading_Image('pipe_body.png'),
            # GIF file format is nor supported by pygame
            'WingUp': loading_Image('bird_wing_up.png'),
            'WingDown': loading_Image('bird_wing_down.png')}


def frames_to_msec(frames, Frame_Rate=Frame_Rate):
    """Convert frames to milliseconds at the specified framerate.

    Arguments:
    frames: How many frames to convert to milliseconds.
    Frame_Rate: The framerate to use for conversion.  Default: Frame_Rate.
    """
    return 1000.0 * frames / Frame_Rate


def msec_to_frames(milliseconds, Frame_Rate=Frame_Rate):
    """Convert milliseconds to frames at the specified framerate.

    Arguments:
    milliseconds: How many milliseconds to convert to frames.
    Frame_Rate: The framerate to use for conversion.  Default: Frame_Rate.
    """
    return Frame_Rate * milliseconds / 1000.0


def main():
    """The application's entry point.

    If someone executes this module (instead of importing it, for
    example), this function is called.
    """

    pygame.init()

    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Pygame Flappy Bird')

    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont(None, 32, bold=True)  # default font
    images = loading_Images()

    # the bird stays in the same x position, so bird.x is a constant
    # center bird on screen
    bird = Bird(50, int(WINDOW_HEIGHT/2 - Bird.HEIGHT/2), 2,
                (images['WingUp'], images['WingDown']))

    pipes = deque()

    frame_clock = 0  # this counter is only incremented if the game isn't paused
    score = 0
    done = paused = False
    while not done:
        clock.tick(Frame_Rate)

        # Handle this 'manually'.  If we used pygame.time.set_timer(),
        # pipe addition would be messed up when paused.
        if not (paused or frame_clock % msec_to_frames(PipePair.ADD_INTERVAL)):
            pp = PipePair(images['endPipe'], images['bodyPipe'])
            pipes.append(pp)

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = True
                break
            elif e.type == KEYUP and e.key in (K_PAUSE, K_p):
                paused = not paused
            elif e.type == MOUSEBUTTONUP or (e.type == KEYUP and
                    e.key in (K_UP, K_RETURN, K_SPACE)):
                bird.msec_to_climb = Bird.CLIMB_DURATION

        if paused:
            continue  # don't draw anything

        # check for collisions


        for x in (0, WINDOW_WIDTH / 2):
            display_surface.blit(images['game_background'], (x, 0))

        while pipes and not pipes[0].visible:
            pipes.popleft()

        for p in pipes:
            p.update()
            display_surface.blit(p.image, p.rect)

        bird.update()
        display_surface.blit(bird.image, bird.rect)

        # update and display score
        for p in pipes:
            if p.x + PipePair.WIDTH < bird.x and not p.score_counted:
                score += 1
                p.score_counted = True


        pygame.display.flip()
        frame_clock += 1
    print('Game over! Score: %i' % score)
    pygame.quit()


if __name__ == '__main__':
    # If this module had been imported, __name__ would be 'flappybird'.
    # It was executed (e.g. by double-clicking the file), so call main.
    main()
