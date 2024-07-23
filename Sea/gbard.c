#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

#define MAX_LINE 80

int main(void) {
    char *args[MAX_LINE/2 + 1]; /* command line arguments */
    char cmd[MAX_LINE + 1];     /* command line */
    int should_run = 1;         /* flag to determine when to exit program */
    int status;                 /* status of child process */

    while (should_run) {
        printf("my_shell> ");
        fflush(stdout);

        /* read user input */
        if (fgets(cmd, MAX_LINE, stdin) == NULL) {
            break;
        }

        /* remove trailing newline */
        cmd[strcspn(cmd, "\n")] = '\0';

        /* parse command line */
        char *token = strtok(cmd, " ");
        int i = 0;
        while (token != NULL) {
            args[i] = token;
            token = strtok(NULL, " ");
            i++;
        }
        args[i] = NULL;

        /* execute command */
        pid_t pid = fork();
        if (pid < 0) {
            perror("fork failed");
            exit(1);
        } else if (pid == 0) {
            /* child process */
            if (execvp(args[0], args) < 0) {
                perror("execvp failed");
                exit(1);
            }
        } else {
            /* parent process */
            waitpid(pid, &status, 0);
        }
    }

    return 0;
}
