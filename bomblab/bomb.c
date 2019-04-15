/****************************************
 * bomb_main.c
 *
 * Thanks to Zhuoqun (Tom) Cheng
 *****************************************/
#include <stdio.h>
#include <stdlib.h>

/* bomb is built by `gcc -Og -o bomb bomb_src.c bomb.c`
 * all these functions are defined in bomb.c, which will
 * be released after Tuesday */

int
main()
{
	char *input;

	printf("Welcome to the lab, enter your inputs below\n");
	/* get input */
	input = read_line();
	phase_1(input);
	printf("Phase 1 Passed!\n");

	/* get input */
	input = read_line();
	phase_2(input);
	printf("Phase 2 Passed!\n");
	printf("Bomb Defused!\n");

	return 0;
}

