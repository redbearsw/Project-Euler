#include <stdio.h>
#include <stdlib.h>


int next(int i, int prev) {
    return i + prev;
}

int p2 (int bound) {
    int sum = 0;
    int i = 2;
    int prev = 1;
    while (i < bound) {
        if (!(i % 2))
            sum += i;
        int j = i;
        i = next(i, prev);
        prev = j;
    }
    return sum;
}

int main() {
    printf("%d\n", p2(90));
    printf("%d\n", p2(4000000));
}
