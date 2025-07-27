#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char s[14];
    scanf("%s", s);
    int sm = 0;
    int idx;
    for (int i=0; i<12; i++) {
        if (s[i]=='*') {
            idx = i;
            continue;
        }
        sm += (s[i] - '0') * (i%2==0 ? 1 : 3);
        // printf("%d\n", sm);
    }
    int res = -1;
    for (int d=0; d<=9; d++) {
        int total = sm + d * (idx % 2 == 0 ? 1 : 3);
        int check = (total % 10 == 0) ? 0 : (10 - total % 10);
        if (check == s[12]-'0') {
            res = d;
            break;
        }
    }
    printf("%d\n", res);
    return 0;
}
