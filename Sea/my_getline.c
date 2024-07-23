#include <stdio.h>
#include <stdlib.h>

ssize_t my_getline(char **lineptr, size_t *n, FILE *stream) {
    ssize_t nread = 0;
    size_t pos = 0;

    if (*lineptr == NULL) {
        *n = 128; // initial buffer size
        *lineptr = malloc(*n);
        if (*lineptr == NULL) {
            return -1; // error: unable to allocate memory
        }
    }

    while (1) {
        int c = fgetc(stream);

        if (c == EOF || c == '\n') {
            (*lineptr)[pos] = '\0'; // terminate the string
            break;
        }

        (*lineptr)[pos] = c;
        pos++;

        if (pos >= *n) {
            *n += 128; // increase buffer size
            char *new_ptr = realloc(*lineptr, *n);
            if (new_ptr == NULL) {
                return -1; // error: unable to allocate memory
            }
            *lineptr = new_ptr;
        }
    }

    if (pos == 0 && nread == EOF) {
        return -1; // error: no input read
    }

    return pos;
}
