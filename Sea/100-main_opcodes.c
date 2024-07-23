/*Write a program that prints the opcodes of its own main function.

    Usage: ./main number_of_bytes
    Output format:
        the opcodes should be printed in hexadecimal, lowercase
        each opcode is two char long
        listing ends with a new line
        see example
    You are allowed to use printf and atoi
    You have to use atoi to convert the argument to an int
    If the number of argument is not the correct one, print Error, followed by a new line, and exit with the status 1
    If the number of bytes is negative, print Error, followed by a new line, and exit with the status 2
    You do not have to compile with any flags

Note: if you want to translate your opcodes to assembly instructions, you can use, for instance udcli.*/

#include <stdio.h>
#include <stdlib.h>

/**
 * main - Prints opcode of own main function
 * @argc: argument count
 * @argv: array of arguments
 * Return: 1 0r 2 on fail, 0 on success
 */
int main(int argc, char *argv[])
{
	int bytes, i;
	int (*address)(int, char **) = main;
	unsigned char opcode;

	if (argc != 2)
	{
		printf("Error\n");
		exit(1);
	}

	bytes = atoi(argv[1]);
	if (bytes < 0)
	{
		printf("Error\n");
		exit(2);
	}

	for (i = 0; i < bytes; i++)
	{
		opcode = *(unsigned char *)address;
		printf("%.2x", opcode);

		if (i == bytes -1)
			continue;
		printf(" ");

		i++;
	}
	printf("\n");
	return (0);
}
