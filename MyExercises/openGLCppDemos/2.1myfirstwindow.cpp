#include <GL/freeglut.h>


void myInit(void)
{
	glClearColor(1.0, 1.0, 1.0, 0.0);
	glColor3f(0.0f, 0.0f, 0.0f);
	glPointSize(4.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, 640.0, 0.0, 480.0);
}

void myDisplay()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_POINTS);
	glVertex2i(100, 50);
	glVertex2i(100, 130);
	glVertex2i(150, 130);
	glEnd();
	glFlush();
}

void drawDot(GLfloat x, GLfloat y)
{
	glBegin(GL_POINTS);
	glVertex2i(x, y);
	glEnd();
}

struct GLintPoint {
	GLfloat x, y;
};

void slerpinski_render()
{
	glClear(GL_COLOR_BUFFER_BIT);
	GLintPoint T[] = { {10,10},{600,10 },{300,600 } };
	int index = rand() % 3;
	GLintPoint point = T[index];
	drawDot(point.x, point.y);
	for (int i = 0; i < 500000; i++)
	{
		index = rand() % 3;
		point.x = (point.x + T[index].x) / 2;
		point.y = (point.y + T[index].y) / 2;
		drawDot(point.x, point.y);
	}
	glFlush();	
}


void drawLine(GLint x1, GLint y1, GLint x2, GLint y2)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_LINES);
	glLineWidth(4.0);
	glColor3f(1, 0, 0);
	glVertex2i(x1, y1);
	glVertex2i(x2, y2);
	glEnd();
	glFlush();
}

void drawLine2()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_LINES);
	glVertex2i(20, 20);
	glVertex2i(300, 300);
	glEnd();
	glFlush();
}

void drawLine3()
{
	glClear(GL_COLOR_BUFFER_BIT);
	drawLine(30, 30, 200, 200);
}

int main(int argc, char ** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(640, 480);
	glutInitWindowPosition(100, 150);
	glutCreateWindow("My first window attempt");
	//glutDisplayFunc(myDisplay);
	//glutDisplayFunc(slerpinski_render);
	glutDisplayFunc(drawLine3);
	myInit();
	glutMainLoop();
	return 0;
}