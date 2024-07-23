#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

extern char **environ;

int count_args(char *line) {
  int count = 0;
  while (line[count] != '\0' && line[count] != ' ') {
    count++;
  }
  return count;
}

int main() {
  char line[100];
  char *command, **args;
  char *path;
  int status;

  while (1) {
    printf("simple_shell> ");
    fflush(stdout);

    if (fgets(line, 100, stdin) == NULL) {
      break;
    }

    command = strtok(line, " ");

    if (command == NULL) {
      continue;
    }

    args = malloc(sizeof(char *) * (count_args(line) + 1));
    args[0] = command;
    int i = 1;
    while (args[i - 1] = strtok(NULL, " ")) {
      i++;
    }

    path = getenv("PATH");

    if (path == NULL) {
      printf("PATH environment variable not set\n");
      continue;
    }

    char *dir;
    char *full_path;

    for (dir = strtok(path, ":"); dir != NULL; dir = strtok(NULL, ":")) {
      full_path = malloc(strlen(dir) + strlen(command) + 2);
      strcpy(full_path, dir);
      strcat(full_path, "/");
      strcat(full_path, command);

      if (access(full_path, F_OK) == 0) {
        pid_t pid = fork();

        if (pid == 0) {
          int argc = count_args(line);
          execve(full_path, args, environ);
          perror(command);
          exit(1);
        }

        break;
      }

      free(full_path);
    }

    if (dir == NULL) {
      printf("Command not found\n");
    }

    wait(&status);
  }

  return 0;
}
