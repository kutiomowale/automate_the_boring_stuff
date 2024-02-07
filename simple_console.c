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
    		if (strcmp("help", response) == 0)
        		printf("%s", help_text);
		else if (strcmp("credits", response) == 0)
        		printf("%s", credit_text);
		else if (strcmp("exit", response) == 0)
		{
        		printf("%s", credit_text);
        		printf("Bye\n");
			break;
		}
    		else
        		printf("Unknown command\n");
	}
}
