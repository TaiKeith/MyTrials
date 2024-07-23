#include <stdio.h>
#include <string.h>

/**
 * we'll need a string consisting of binary only
 * 1   0   1   1
 * 2^3 2^2 2^1 2^0
 * 8 + 0 + 2 + 1 = 11
 */

int binary_to_decimal(char *string);
/**
 * binary_to_decimal - A function that converts binary to decimal
 * @string: A pointer to string of binary
 *
 * Return: Converted decimal from binary
 */

int main(void)
{
	char s1[] = "1011";
	int val1 = binary_to_decimal(s1);
	printf("s1 in decimal is: %d\n", val1);

	return (0);
}

int binary_to_decimal(char *string)
{
	int total = 0, decval = 1;
	int slen = strlen(string);
	int i;

	for (i = (slen - 1); i >= 0; i--)
	{
		if (string[i] == '1')
		{
			total += decval;
			decval *= 2;
		}
		return (total);
	}
}
