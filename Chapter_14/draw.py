from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
window_screen = pygame.display.set_mode((640, 480), HWSURFACE|OPENGL|DOUBLEBUF)

#Draw a geometry for the scene
def Draw():
       #translation (moving) about 6 unit into the screen and 1.5 unit to left
       glTranslatef(-1.5,0.0,-6.0)
       glBegin(GL_TRIANGLES) #GL_TRIANGLE is constant for TRIANGLES        
       glVertex3f( 0.0, 1.0, 0.0) #first vertex       
       glVertex3f(-1.0, -1.0, 0.0)  #second vertex   
       glVertex3f( 1.0, -1.0, 0.0) #third vertex     
       glEnd()

Draw()
