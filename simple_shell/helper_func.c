#include "shell.h"

char *replace_var(const char *token, char *buffer, size_t buf);

/**
 * replace_variable - replaces variables with their values in the token
 * @token: input token
 * @buffer: buffer to store the result
 * @bufsize: size of the buffer
 * Return: pointer to the result buffer
 */
char *replace_variable(const char *token, char *buffer, size_t bufsize)
{
    char *result = buffer;
    size_t len = strlen(token);

    for (size_t i = 0; i < len && bufsize > 1; i++)
    {
        if (token[i] == '$')
        {
            i++;
            if (i >= len)
                break;

            if (token[i] == '?')
            {
                // Replace with exit status of the last command
                int exit_status = WIFEXITED(last_status) ? WEXITSTATUS(last_status) : -1;
                bufsize -= snprintf(buffer, bufsize, "%d", exit_status);
                buffer += (bufsize > 1) ? strlen(buffer) : 0;
            }
            else if (token[i] == '$')
            {
                // Replace with the process ID of the shell
                bufsize -= snprintf(buffer, bufsize, "%d", getpid());
                buffer += (bufsize > 1) ? strlen(buffer) : 0;
            }
            else
            {
                // Ignore unknown variables
                *buffer++ = '$';
                bufsize--;
                i--;
            }
        }
        else
        {
            *buffer++ = token[i];
            bufsize--;
        }
    }
    *buffer = '\0';
    return (result);
}
