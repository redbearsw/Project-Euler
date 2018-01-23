#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int long pythag(int lim) {
	int a,b,c;
	for (b = floor(lim / 3); b < lim - 2; b++) {
		for (c = ceil(lim / 3), a = (lim - b - c); a > 0 && c < lim - 2; a--, c++) {
			if ((a * a) + (b * b) == (c * c))
				return a * b * c;
		}
	}
	return 0;
}

int long pyth_mathy(int lim) {
	double a, b;
	int c, a_int;
	for (b = 1.0; b < lim; b++) {
		a = (500000 - 1000 * b) / (1000 - b);
		int a_int = a;
		if (a / a_int == 1) {
			c = 1000 - a - b;
			return a * b * c;
		}
	}
	return 0;
}
	


int main() {
	int long answer12 = pythag(12);
	int long answer = pythag(1000);
	int long answer30 = pythag(30);
	int long answer_mathy = pyth_mathy(1000);	
	printf("pythag trip (12) = %ld\n",answer12);
	printf("pythage trip (30) = %ld\n",answer30);
	printf("pythag trip (1000) = %ld or %ld\n",answer,answer_mathy);
}
