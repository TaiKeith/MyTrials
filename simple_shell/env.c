#include <stdio.h>

extern char** environ;

int main(int argc, char* argv[], char* env[])
{
	// Print the addresses of env (third parameter) and environ (global variable)
	printf("Address of env: %p\n", env);
    	printf("Address of environ: %p\n", environ);

    	// Check if the addresses are the same
    	if (env == environ)
	{
        	printf("The addresses of env and environ are the same.\n");
    	} else {
        	printf("The addresses of env and environ are different.\n");
    	}

    	return 0;
}
