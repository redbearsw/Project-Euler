#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int palindrome_check(int number) {
	int length = 0; int num;
	for(num = number; num > 0; num = num / 10) {
		length++;
	}
	
	int array[length]; int i;
	for(i = 0; i < length; i++) {
		array[i] = (number % (int) pow(10.0, i + 1)) / pow(10, i);
	}

	
	
	int count = 0;
	for(i = 0; i < (length / 2); i++) {
		if (array[i] == array[length - 1 - i])
			count++;
	}
	if (count == (length / 2))
		return 1;
	else
		return 0;
}


int largest_pal()
{
	int i; int j; int result = 0;
	for (i = 0; i < 1000; i++) {
		for(j = 0; j < 1000; j++) {
			if (palindrome_check(i * j) == 1)
				if (i * j > result)
					result = i * j;
		}
	}
	return result;
}

int main()
{
	int result1 = palindrome_check(1331);
	int result2 = palindrome_check(12341);
	int result3 = palindrome_check(1234321);
	printf("1331: %d, 12341: %d, 1234321: %d\n",result1,result2,result3);
	int answer = largest_pal();
	printf("answer: %d\n",answer);
}
