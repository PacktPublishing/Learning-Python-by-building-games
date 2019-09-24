from OpenGL.GL import *
from OpenGL.GLU import *

cube_Vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )

cube_Edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

cube_Surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)    
    )


def renderCube():
    glBegin(GL_QUADS)
    for eachSurface in cube_Surfaces:
        for eachVertex in eachSurface:
            glColor3fv((1, 1, 0)) #yellow color code
            glVertex3fv(cube_Surfaces[eachVertex])
    glEnd()
    glBegin(GL_LINES)
    for eachEdge in cube_Edges:
        for eachVertex in eachEdge:
            glVertex3fv(cube_Vertices[eachVertex])
    glEnd()

def ActionHandler():
    pygame.init()
    screen = (800, 500)
    pygame.display.set_mode(screen, DOUBLEBUF|OPENGL) #OPENGL is essential
    
    #1: ADD A CLIPPING TRANSFORMATION
    gluPerspective(85.0, (screen[0]/screen[1]), 0.1, 50) 
    
    # 80.0 -> field view of camera 
    #screen[0]/screen[1] -> aspect ration (width/height)
    #0.1 -> near clipping plane
    #50 -> far clipping plane
    glRotatef(18, 2, 0, 0) #start point
    while True:

        for anyEvent in pygame.event.get():
            if anyEvent.type == pygame.QUIT:
                pygame.quit()
                quit()

            if anyEvent.type == pygame.MOUSEBUTTONDOWN:
                print(anyEvent)
                print(anyEvent.button) #printing mouse event
                
                #mouse button 4 and 5 are at the left side of the mouse
                #mouse button 4 is used as forward and backward navigation
                if anyEvent.button == 4: 
                    glTranslatef(0.0,0.0,1.0) #produces translation of (x, y, z)
                elif anyEvent.button == 5:
                    glTranslatef(0.0,0.0,-1.0)

                glRotatef(1, 3, 1, 1) 
#The glRotatef is used to perform matrix transformation which performs a rotation 
#of counterclockwise with an angle of degree about origin through the point #provided as (x, y, z). 
        #-----------------------------------------------------------------
        #indicates the buffer that needs to be cleared
        #GL_COLOR_BUFFER_BIT: enabled for color drawing
        #GL_DEPTH_BUFFER_BIT: depth buffer which needs to be cleared
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #render cube
        renderCube()
        pygame.display.flip()
        pygame.time.wait(12)

#call main function only externally
ActionHandler()
