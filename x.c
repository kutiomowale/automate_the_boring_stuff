#include <stdio.h>

/**
 * main - A default C file
 * Return: Always 0
 */
int main(void)
{
	char str[1000];

	printf("length of fish: %d\n", strlen("fish"));
	scanf("%s", str);
	printf("length of %s: %d\n", str, strlen(str));
	printf("vv == hh: %d\n", strcmp("vv", "hh"));
	printf("cat == ca: %d\n", strcmp("cat", "ca"));
	printf("ca == cat: %d\n", strcmp("ca", "cat"));

	return (0);
}
