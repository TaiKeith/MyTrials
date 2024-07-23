#include "shell.h"

/**
 * cha - A function that
 * @:
 */
void change_dir(int ac, char *argv[])
{
	char *path = NULL;
	char current_dir[MAX_COMMANDS];
	char new_dir[MAX_COMMANDS];

	getcwd(current_dir, MAX_COMMANDS);

	if (ac > 1)
	{
		path = argv[1];
	}

	if (path == NULL)
	{
		path = getenv("HOME");
	}
	else if (_strcmp(path, "-") == 0)
	{
		path = getenv("OLDPWD");
		if (path == NULL)
		{
			perror("OLDPWD environment variable not set");
			return;
		}
	}

	if (chdir(path) == 0)
	{
		_setenv(argv);
		getcwd(new_dir, MAX_COMMANDS);
		setenv("PWD", new_dir, 1);
	}
	else
	{
		perror("cd");
	}
}
