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

long int mult_arr(int arr[], int arr_sz) {
	long int prod = 1;
	int i;
	for (i = 0; i < arr_sz; i++)
		prod *= arr[i];
	return prod;
}

long int larg_prod_13arr(char* filename, int num_prod) {
	FILE* fp = fopen(filename, "r");
	char c; int i; int arr[num_prod];
	int place = 0; int prod;
	for (i = 0; i < num_prod; i++) {
		c = fgetc(fp);
		arr[i] = c - '0';
	}
	prod = mult_arr(arr, num_prod);
	int dig;
	while (!feof(fp)) {
		c = fgetc(fp);
		dig = c - '0';
		if (dig > arr[place]) {
			if (arr[0] != 0) {
				prod = prod * dig / arr[0];
				arr[place] = dig;
			}
			else {
				arr[place] = dig;
				mult_arr(arr, num_prod);
			}
		}
		place++;
		place = place % num_prod;
	}
	return prod;
}
		
		
			


int main() {
	long int answer = larg_prod_from_file(1000, "p8_number.txt", 13);
	long int answer4 = larg_prod_from_file(1000, "p8_number.txt", 4);
	printf("largest product = %ld\n",answer);
	printf("largest product (4) = %ld\n",answer4);

	long int answer_arr = larg_prod_13arr("p8_number.txt", 13);
	printf("from array: %ld\n",answer_arr);

}
