#include <stdio.h>
#include <stdlib.h>

int sum_sq_diff(int num) {
	int sum_sq = 0;
	int sq_sum = 0;
	int i;
	for (i = 1; i < num + 1; i++) {
		sum_sq += i*i;
	}
	for (i = 1; i < num + 1; i++)
		sq_sum += i;
	sq_sum = sq_sum * sq_sum;
	return sq_sum - sum_sq;
}


int main() {
	int s10 = sum_sq_diff(10);
	int s100 = sum_sq_diff(100);
	printf("10: %d, 100: %d\n",s10,s100);
}
