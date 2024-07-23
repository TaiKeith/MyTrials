#include <stdio.h>
#include <string.h>

int isPalindrome(char *str, int start, int end)
{
	if (start >= end)
	{
		return (1);
	}
	else
	{
		if (str[start] == str[end])
		{
			return isPalindrome(str, start + 1, end - 1);/*recurive call*/
		}
		else
		{
			return (0);
		}
	}
}

int main()
{
	char *str;
	printf("Enter string:\n", str);
	scanf("%s", str);

	int len = strlen(str);
	int Palindrome = isPalindrome(str, 0, len - 1);

	if (Palindrome)
	{
		printf("%s is a palindrome\n", str);
	}
	else
	{
		printf("%s is not a palindrome\n", str);
	}
}
