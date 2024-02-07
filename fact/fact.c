#include <stdio.h>

long int fact(int num);

/**
 * main - Using the fact function defined below.
 * Return: Always 0.
 */
int main(void)
{
	printf("fact(1599) = %ld\n", fact(1599));
	printf("fact(3) = %ld\n", fact(3));
	printf("fact(31) = %ld\n", fact(31));
	printf("**8222838654177922817725562880000000**\n");
	return (0);
}

/**
 * fact - Return the factorial of integer @num
 * @num: The integer
 * Return: Factorial of @num
 * Returns 1 if a negative integer is passed
 */
long int fact(int num)
{
	long int res;

	res = 1;
	while (num > 0)
	{
		res = res * num;
		num = num - 1;
	}
	return (res);
}
