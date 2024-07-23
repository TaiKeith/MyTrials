#include <stdio.h>

int main()
{
	char command[100];
	printf("$ ");
	fgets(command, 100, stdin);
	printf("%s", command);
	return (0);
}
