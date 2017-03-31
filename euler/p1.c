#include <stdlib.h>
#include <stdio.h>

int p1(int bound) {
    int i;
    int sum = 0;
    for (i = 0; i < bound; i++) {
        sum += (!(i % 3) * i) + (!(i % 5) * i) - (!(i % 15) * i);
    }
    return sum;
}

int main() {
    printf("%d\n", p1(1000));
}
