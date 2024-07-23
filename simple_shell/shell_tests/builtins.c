#include "shell.h"

/**
 * exit_func - implementation of the exit built-in command
 * Return: exit status
 */
void exit_func(int status)
{
	exit(status);
}
/**
 * env_func - implementation the env built-in command
 * @argv: array of char pointers representing the arguments passed to the
 * env command
 */
void env_func(char *argv[])
{
	char **env = environ;
	(void)argv;

	while (*env != NULL)
	{
		printf("%s\n", *env);
		env++;
	}
}
