#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// This function prints the prompt and waits for user input.
char *get_user_input() {
  char *buffer = malloc(1024);
  fgets(buffer, 1024, stdin);
  buffer[strlen(buffer) - 1] = '\0';
  return buffer;
}

// This function parses the user input and executes the corresponding command.
void execute_command(char *command) {
  // Split the command into words.
  char *words[1024];
  int num_words = 0;
  char *token = strtok(command, " ");
  while (token != NULL) {
    words[num_words++] = token;
    token = strtok(NULL, " ");
  }

  // Check if the command is built-in.
  if (strcmp(words[0], "cd") == 0) {
    // Change directory.
    if (chdir(words[1]) != 0) {
      perror("chdir");
    }
  } else if (strcmp(words[0], "pwd") == 0) {
    // Print working directory.
    char cwd[1024];
    if (getcwd(cwd, 1024) == NULL) {
      perror("getcwd");
    }
    printf("Current directory: %s\n", cwd);
  } else if (strcmp(words[0], "exit") == 0) {
    // Exit the shell.
    exit(0);
  } else {
    // Execute the command as a system command.
    if (system(command) != 0) {
      perror("system");
    }
  }
}

// This is the main function of the shell.
int main() {
  // Print the prompt and start the loop.
  char *prompt = "myshell$ ";
  while (1) {
    printf(prompt);
    char *command = get_user_input();
    if (command == NULL) {
      break;
    }
    execute_command(command);
  }
  return 0;
}
