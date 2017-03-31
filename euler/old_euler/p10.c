#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int prime(int num) {
	int div;
	for (div = 2; div < sqrt(num) + 1; div++)
		if (num % div == 0)
			return 0;
	return 1;
}

long int sum_primes(int lim) {
	long int j; long int sum = 2;
	for (j = 3; j < lim; j += 2) {
		if (prime(j))
			sum += j;
	}
	return sum;
}

long int sum_primes_array(int lim) {
	int i; long int sum = 2;
	int len = ceil(lim / 2) - 1;
	int arr[len];
	int j = 3;
	for (i = 0; i < len; i++, j += 2)
		arr[i] = j;
	for (i = 0; i < len; i++) {
		if (arr[i] == 0)
			continue;
		else if (prime(arr[i])) {
			for (j = i + arr[i]; j < len - i; j += arr[i])
				arr[j] = 0;
			sum += arr[i];

		}
	}
	return sum;
}

int main() {
	long int sum10 = sum_primes(10);
	long int sum = sum_primes(2000000);
	long int sum_arr10 = sum_primes_array(10);
	long int sum_arr = sum_primes_array(2000000);	
	printf("10: %ld, 2,000,000: %ld\n",sum10,sum);
	printf("10: %ld, 2,000,000: %ld\n",sum_arr10,sum_arr);
}
