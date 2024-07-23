#include "shell.h"

/**
 * main - Entry point
 * @ac: argument count
 * @av: argument vector
 * Return: 0
 */


int main(int ac, char *av[])
{
	char *prompt = "(myShell)$ ";
	char *command = NULL;
	char *argv[MAX_ARGS];
	size_t bufsize = BUFF_SIZE;
	ssize_t cmdread;
	pid_t pid;
	int status;
	(void)ac;

	while (1)
	{
		printf("%s", prompt);
		cmdread = getline(&command, &bufsize, stdin);

		if (cmdread == -1)
		{
			printf("\n");
			return (-1);
		}
		printf("%s", command);
		parse_func(command, argv);

		av[0] = argv[0];
		pid = fork();
		if (pid < 0)
		{
			free(command);
			perror("fork");
			exit(EXIT_FAILURE);
		}
		else if (pid == 0)
		{
			execve(av[0], argv, environ);
			perror("Error");
			exit(EXIT_FAILURE);
		}
		else
		{
			wait(&status); /*waitpid(pid, &status, 0);*/
		}
	}
	free(command);
	return (0);
}