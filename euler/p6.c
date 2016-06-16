#include <stdio.h>
#include <stdlib.h>

int sum_sq_diff(int num) {
	if (num == 1)
		return 0;
	else
		return sum_sq_diff(num - 1) + ((num * num) * (num - 1));
}

int sum_sq_diff_it(int num) {
	int i; int total = 0;
	for (i = 1; i <= num; i++)
		total += ((i * i) * (i - 1));
	return total;
}		

int main() {
	int d5 = sum_sq_diff(5);
	int d10 = sum_sq_diff(10);
	int d100 = sum_sq_diff(100);
	int d100i = sum_sq_diff_it(100);
	printf("5: %d, 10: %d, 100: %d or %d\n",d5,d10,d100,d100i);
}
