#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    long res = -1;
    char c[9];
    for (int i = 0; i < 3; i++) {
        scanf("%s", c);
        char* end;
        long num = strtol(c, &end, 10);
        if (end!=c) {
            res = num + (3-i);
        }
    }
    if (res%3 != 0 && res%5 != 0) {
        printf("%ld\n", res);
    } else if (res%3 == 0 && res%5 != 0) {
        printf("Fizz\n");
    } else if (res%3 != 0 && res%5 == 0) {
        printf("Buzz\n");
    } else {
        printf("FizzBuzz\n");
    }
    return 0;
}
