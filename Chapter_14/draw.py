import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

window_screen = pygame.display.set_mode((640, 480),
                                        HWSURFACE | OPENGL | DOUBLEBUF)


#Draw a geometry for the scene
def Draw():
    # translation (moving) about 6 unit into the screen and 1.5 unit to left
    glTranslatef(-1.5, 0.0, -6.0)
    glBegin(GL_TRIANGLES)  # GL_TRIANGLE is constant for TRIANGLES
    glVertex3f(0.0, 1.0, 0.0)  # first vertex
    glVertex3f(-1.0, -1.0, 0.0)  # second vertex
    glVertex3f(1.0, -1.0, 0.0)  # third vertex
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Draw()
        pygame.display.flip()
        pygame.time.wait(12)


main()
