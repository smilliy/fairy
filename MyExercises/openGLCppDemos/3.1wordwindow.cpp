#include <GL/freeglut.h>
#include <cmath>

const float pi = 3.14159265358;

void setWindow(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top)
{
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(left, right, bottom, top);
}

void setViewport(GLint left, GLint right, GLint bottom, GLint top)
{
	glViewport(left, bottom, right - left, top - bottom);
}

void myDisplay()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glBegin(GL_LINE_STRIP);
	for (float x = -4.0; x < 4.0; x += 0.1)
	{
		if (x == 0.0)
			glVertex2f(0.0, 1.0);
		else
			glVertex2f(x, sin(pi*x) / (pi*x));
	}
	glEnd();
	glFlush();
}

void myInit()
{
	glClearColor(1.0, 1.0, 1.0, 0.0);
	glColor3f(0.0f, 0.0f, 1.0f);
	glLineWidth(2.0);
}

int main(int argc, char ** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(640, 480);
	glutInitWindowPosition(100, 150);
	glutCreateWindow("The famous sinc function");
	glutDisplayFunc(myDisplay);
	myInit();
	setWindow(-5.0, 5.0, -0.3, 1.0);
	setViewport(0, 640, 0, 480);
	glutMainLoop();
	return 0;
}
