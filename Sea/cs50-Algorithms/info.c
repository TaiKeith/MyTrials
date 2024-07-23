#include "info.h"

int main(void)
{
	person people[] = {
		{"Carter", "+254-712-345-678", "carter@gmail.com"},
		{"Dave", "+254-789-654-321", "dave@hotmail.com"},
		{"Kris", "+254-123-456-789", "kallmekris@hotmail.com"}
	};

	for (int i = 0; i < 3; i++)
	{
		printf("Contact list info for %s:\n", people[i].name);
		printf("\tPhone number: %s\n", people[i].number);
		printf("\tEmail: %s\n", people[i].email);
		printf("\n");
	}
	return 0;
}
