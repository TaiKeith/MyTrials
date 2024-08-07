#include "shell.h"

/**
 * file_path - A function that gets the PATH environment variable of a command
 * and executes the command
 * @argv: pointer to a character
 */

void file_path(char *argv[])
{
	char *path, *path_copy;
	char *dir;
	char full_path[BUFF_SIZE];
	int status;
	size_t len;

	path = getenv("PATH");
	printf("PATH: %s\n", path);
	path_copy = strdup(path);

	if (path == NULL)
	{
		write(STDOUT_FILENO, "PATH environment variable not found\n", 35);
		return;
	}

	dir = strtok(path_copy, ":");
	while (dir != NULL)
	{
		len = strlen(dir);
		strncpy(full_path, dir, BUFF_SIZE - 1);
		full_path[BUFF_SIZE - 1] = '\0';
		/*strcat(full_path, "/");
		strcat(full_path, argv[0]);*/

		if (dir[len - 1] != '/')
		{
			strcat(full_path, "/");
		}

		strcat(full_path, argv[0]);

		printf("Full Path: %s\n", full_path);


		if (access(full_path, F_OK) == 0)
		{
			pid_t pid = fork();

			if (pid < 0)
			{
				perror("fork");
				exit(EXIT_FAILURE);
			}
			else if (pid == 0)
			{
				printf("Executing: %s\n", full_path);
				execve(full_path, argv, environ);
				perror("execve");
				exit(EXIT_FAILURE);
			}
			else
			{
				waitpid(pid, &status, 0);
				free(path_copy);
				if (WIFEXITED(status) && WEXITSTATUS(status) == 0)
				{
					return;
				}
			}
		}

		dir = strtok(NULL, ":");
	}
	free(path_copy);
	write(STDOUT_FILENO, "Command not found\n", 18);
}
