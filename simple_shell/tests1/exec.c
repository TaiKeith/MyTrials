#include "shell.h"

/**
 * get_full_path - a fuction that gets the full path
 * @dir: function parameter 1
 * @command: function parameter 2
 * @full_path: function parameter 3
 * Return: Full path if found and executable, otherwise NULL
 */
char *get_full_path(char *dir, const char *command, char full_path[])
{
	strncpy(full_path, dir, BUFF_SIZE - 1);
	full_path[BUFF_SIZE - 1] = '\0';
	_strcat(full_path, "/");
	_strcat(full_path, command);

	if (access(full_path, X_OK) != 0)
	{
		return (NULL);
	}
	return (full_path);
}

/**
 * exec_command_path - handles the actual execution of the command
 * @full_path: function parameter 1
 * @argv: array pointer to a character
 * Return: 0 on success, otherwise -1 on failure
 */
int exec_command_path(char *full_path, char *argv[])
{
	int status;
	pid_t pid = fork();

	if (pid < 0)
	{
		perror("fork");
		return (-1);
	}
	else if (pid == 0)
	{
		execve(full_path, argv, environ);
		perror("execve");
		return (-1);
	}
	else
	{
		waitpid(pid, &status, 0);
		if (WIFEXITED(status) && WEXITSTATUS(status) == 0)
		{
			return (0);
		}
		else
		{
			return (-1);
		}
	}
}

/**
 * find_exec_command - function is responsible for traversing the PATH
 * environment variable and finding the full path of the executable
 * @argv: pointer to a string
 * Return: Full path of the executable if found, otherwise NULL
 */
char *find_exec_command(char *argv[])
{
	char *path = _getenv("PATH");
	char *path_copy = strdup(path);
	char *dir = strtok(path_copy, ":");
	char full_path[BUFF_SIZE];
	char *result;

	if (path == NULL)
	{
		write(STDOUT_FILENO, "PATH environment variable notfound\n", 35);
		return (NULL);
	}
	if (path_copy == NULL)
	{
		perror("strdup");
		exit(EXIT_FAILURE);
	}
	while (dir != NULL)
	{
		if (argv[0][0] == '/')
		{
			if (access(argv[0], F_OK) == 0)
			{
				/*exec_command_path(argv[0], argv);*/
				free(path_copy);
				return (argv[0]);
			}
			break;
		}

		result = get_full_path(dir, argv[0], full_path);

		if (result != NULL)
		{
			free(path_copy);
			return (result);
		}
		dir = strtok(NULL, ":");
	}
	free(path_copy);
	return (NULL);
}

/**
 * file_path -simple wrapper around the core functionality provided
 * by find_exec_command
 * @argv: pointer to an array
 */
void file_path(char *argv[])
{
	char *full_path = find_exec_command(argv);

	if (full_path != NULL)
	{
		exec_command_path(full_path, argv);
	}
	else
	{
		write(STDOUT_FILENO, "No such file or directory\n", 26);
	}
}

/**
 * run_script -handles the non-interactive mode of the shell
 * @file_stream: name of the script file to execute
 */
void run_script(FILE *file_stream)
{
	char *line = NULL;
	size_t  bufsize = 0;
	ssize_t line_len;

	while ((line_len = getline(&line, &bufsize, file_stream)) != -1)
	{
		line[strcspn(line, "\n")] = '\0';

		parse_exec_command(line);
	}
	free(line);
}
