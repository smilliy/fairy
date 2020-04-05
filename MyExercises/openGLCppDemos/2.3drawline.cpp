#include <GL/freeglut.h>

constexpr int RED = 1;
constexpr int GREEN = 2;
constexpr int BLUE = 3;
constexpr int WHITE = 4;
float angle = 0.0;
float red = 1.0, blue = 1.0, green = 1.0;

void processMenuEvents(int option)
{
	switch (option)
	{
	case RED: red = 1.0; green = 0.0; blue = 0.0;break;
	case GREEN: red = 0.0; green = 1.0; blue = 0.0; break;
	case BLUE: red = 0.0; green = 0.0; blue = 1.0; break;
	case WHITE: red = 1.0; green = 1.0; blue = 1.0; break;
	default:
		break;
	}
}

void renderScene()
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
	glRotatef(angle, 0.0, 1.0, 0.0);
	glColor3f(red, green, blue);
	glBegin(GL_TRIANGLES);
	glVertex3f(-0.5, -0.5, 0.0);
	glVertex3f(0.5, 0.0, 0.0);
	glVertex3f(0.0, 0.5, 0.0);
	glEnd();
	angle++;
	glutSwapBuffers();
}


int main(int argc, char * argv[])
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	glutInitWindowSize(320, 320);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("Menu Test");
	glutDisplayFunc(renderScene);
	glutIdleFunc(renderScene);
	glutCreateMenu(processMenuEvents);
	glutAddMenuEntry("Red", RED);
	glutAddMenuEntry("Blue", BLUE);
	glutAddMenuEntry("Green", GREEN);
	glutAddMenuEntry("White", WHITE);
	glutAttachMenu(GLUT_RIGHT_BUTTON);
	glutMainLoop();
	return 0;
}
