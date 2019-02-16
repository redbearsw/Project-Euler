#include <stdio.h>
#include <stdlib.h>

void get_input(char* name) {
    FILE *input = fopen(name,"r");
    if (input == NULL) {
        fprintf(stderr, "Can't open file %s\n", name);
        return;
    }
    char c;
    while (fscanf(input, "%c", &c) != EOF) {
        // add to array
    }
    fclose(input);
    return;
}

int main() {
    get_input("day1.txt");
}
