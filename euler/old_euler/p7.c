#include <stdio.h>
#include <math.h>
int prime(int num) {
	int div;
	for (div = 2; div < sqrt(num) + 1; div++)
		if (num % div == 0)
			return 0;
	return 1;
}

int prime_gen(int place) {
	int i = 1; //for 2 being prime
	int j;
	for (j = 3; i < place; j += 2) {
		if (prime(j))
			i++;
	}
	return j - 2;
}

int main() {
	int p6 = prime_gen(6);
	int p7 = prime_gen(7);
	int p10001 = prime_gen(10001);
	printf("6: %d, 7: %d, 10001: %d\n",p6,p7,p10001);
}
		

