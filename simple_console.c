#include <stdio.h>
/**
 * main - A simple console
 * Return: Always 0
 */

int main(void)
{
	char response[100];

	char *welcome_text = "Welcome to SimCon\n";
	char *help_text = "exit to leave\nhelp for help\ncredits for credits\n";
	char *credit_text = "SimCon ©kutiomowale 2024.\n";
	char *prompt_text = "(SimCon) ";

	printf("%s", welcome_text);
	printf("%s", help_text);

	while (1)
	{
    		printf("%s", prompt_text);
    		scanf("%s", response);
    		if strres == 'help':
        print(help_text)
    elif res == 'credits':
        print(credit_text)
    elif res == 'exit':
        print(credit_text)
        print('Bye')
        break
    else:
        print('Unknown command')
}
