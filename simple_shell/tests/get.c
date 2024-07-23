#include "shell.h"

char *_getenv(const char *name)
{
	int i = 0;
	char *env_value;

	for (; environ[i] != NULL; i++)
	{
		if (strncmp(environ[i], name, strlen(name)) == 0)
		{
			env_value = strchr(environ[i], '=');
			return (env_value + 1);
		}
	}
	return (NULL);
}
