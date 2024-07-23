#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_INPUT_LENGTH 1024
#define MAX_ARGS 64

int main() {
    char input[MAX_INPUT_LENGTH];
    char* args[MAX_ARGS];

    while (1) {
        printf("> ");
        fgets(input, MAX_INPUT_LENGTH, stdin);

        int arg_count = 0;
        char* token = strtok(input, " \n");
        while (token != NULL && arg_count < MAX_ARGS) {
            args[arg_count] = token;
            arg_count++;
            token = strtok(NULL, " \n");
        }
        args[arg_count] = NULL;

        if (arg_count > 0) {
            pid_t pid = fork();
            if (pid == 0) {
                execvp(args[0], args);
                perror("execvp");
                exit(EXIT_FAILURE);
            } else if (pid < 0) {
                perror("fork");
            } else {
                int status;
                waitpid(pid, &status, 0);
            }
        }
    }

    return 0;
}
