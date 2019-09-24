from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
from OpenGL.GL import *

"""
we have to install OpenGLContext module which will store all the states that 
are associated with the instances of OpenGL. 
If the context is destroyed then eventually OpenGL will be destroyed.

"""


class TriangleContext( BaseContext ):

    initialPosition = (0, 0, 0)  
    
    #define render
    def Render(self, mode):
        
        """ Render triangle"""
        glDisable(GL_CULL_FACE)
        glTranslatef(-1.5, 0.0, -6.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glEnd()

if __name__ == "__main__":
    TriangleContext.ContextMainLoop()
