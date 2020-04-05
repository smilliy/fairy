#include <GL/freeglut.h>
#include <cmath>

const int screenWidth = 640;
const int screenHeight = 480;
GLdouble A, B, C, D;

void myInit()
{
	glClearColor(1, 1, 1, 0);
	glColor3f(1, 0, 0);
	glPointSize(2);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0, screenWidth, 0, screenHeight);
	A = screenWidth / 4;
	B = 0;
	C = D = screenHeight / 2;
}

void myDisplay()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_POINTS);
	for (GLdouble x = 0; x < 4.0; x += 0.005)
	{
		GLdouble func = exp(-x) * cos(2 * 3.141592653*x);
		glVertex2d(A*x + B, C*func + D);
	}
	glEnd();
	glFlush();
}

int main(int argc, char *argv[])
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(screenWidth, screenHeight);
	glutInitWindowPosition(100, 150);
	glutCreateWindow("Dot Plot of a Function");
	glutDisplayFunc(myDisplay);
	myInit();
	glutMainLoop();
	return 0;
}