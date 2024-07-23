#include <stdlib.h>
#include <stdio.h>

int main() {
    char *name = "MY_VAR";
    char *value = "hello world";
    int overwrite = 1;

    if (setenv(name, value, overwrite) == 0) {
        printf("The environment variable has been set successfully.\n");
    } else {
        perror("Error setting environment variable.");
    }
    return 0;
}
