#include <stdio.h>
#include <stdlib.h>


int smallest_multiple(int max) {
	int num = max;
	int div = max;
	while (div > 1) {
		if (num % div == 0)
			div--;
		else {
			num++;
			div = max;
		}
	}
	return num;
}

int main() {
	int a2 = smallest_multiple(2);
	int a3 = smallest_multiple(3);
	int a4 = smallest_multiple(4);
	int a5 = smallest_multiple(5);
	int a6 = smallest_multiple(6);
	int a10 = smallest_multiple(10);
	int a20 = smallest_multiple(20);
	int a11 = smallest_multiple(11);
	printf("2: %d, 3: %d, 4: %d, 5: %d. 6: %d,10: %d, 11: %d, 20: %d\n",a2,a3,a4,a5,a6,a10,a11,a20);
}
		
			
			

