#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long int larg_prod_from_file(int sz, char* filename, int num_prod) {
	FILE* fp = fopen(filename, "r");
	//necessary variables
	char buf[100]; int len; int i; int j;
	int counter = 0; //for calculating where to place in array
	int number[sz]; //for storing number
	//pull number from file into array
	while (fgets(buf, 100, fp) != NULL) {
		len = strlen(buf);
		buf[len - 1] = '\0';
		for (i = 0; i < len - 1; i++)
			number[i + counter] = buf[i] - '0';
		counter += len - 1;
	}
	//calculate product
	i = 0; int long prod; int long max = 0;
	while (i < sz - num_prod) {
		if (number[i] == 0)
			i++;
		else {
			prod = number[i];
			for (j = i + 1; j < i + num_prod; j++) {
				if (number[j] == 0) {
					i = j + 1;
					break;
				}
				else {
					prod *= number[j];
				}
			}
			if (max < prod)
				max = prod;
			i++;
		}
	}
	return max;
}	


int main() {
	long int answer = larg_prod_from_file(1000, "p8_number.txt", 13);
	long int answer4 = larg_prod_from_file(1000, "p8_number.txt", 4);
	printf("largest product = %ld\n",answer);
	printf("largest product (4) = %ld\n",answer4);

}
