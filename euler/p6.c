#include <stdio.h>
#include <stdlib.h>

int sum_sq_diff(int num) {
	if (num == 1)
		return 0;
	else
		return sum_sq_diff(num - 1) + ((num * num) * (num - 1));
}

int main() {
	int d5 = sum_sq_diff(5);
	int d10 = sum_sq_diff(10);
	int d100 = sum_sq_diff(100);
	printf("5: %d, 10: %d, 100: %d\n",d5,d10,d100);
}
