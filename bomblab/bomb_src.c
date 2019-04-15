/*******************************************
 * bomb.c
 * 
 * Thanks to Zhuoqun (Tom) Cheng
 ********************************************/
#include <stdio.h>
#include <stdlib.h>

char buffer[256];

char *
read_line()
{
	gets(buffer);
	return buffer;
}

void
explode_bomb()
{
	printf("BOOM!!\n");
	exit(0);
}

int
string_length(char *str)
{
	int i = 0;
	while(*(str + i) != '\0') i++;
	return i;
}

int
compare_str(char *input, const char *base)
{
	int res = 1, i, len1, len2;

	len1 = string_length(input);
	len2 = string_length((char *) base);
	if (len1 != len2)
		res = 0;

	for (i = 0; i < len1; i++) {
		if (*(input + i) != *(base + i)) {
			res = 0;
			break;
		}
	}

	return res;
}

void read_two_numbers(char *input, int *number)
{
    sscanf(input, "%d %d", &number[0], &number[1]);
}

void read_three_numbers(char *input, int *number)
{
    sscanf(input, "%d %d %d", &number[0], &number[1], &number[2]);
}

void
phase_1(char *input)
{
	if (!compare_str(input, "Small World"))
		explode_bomb();
}

void
phase_2(char *input)
{
    int number[2];
    
    read_two_numbers(input, number);
 
    if(number[0] < number[1])
    {
	explode_bomb();
    }
}

void
phase3(char *input)
{
    int i;
    int number[3];
    
    read_three_numbers(input, number);
    
    for(i=0;i<3;i++)
    {
	if(number[i] != i*3)
	{
	    explode_bomb();
	}
    }
}

