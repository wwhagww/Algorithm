#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b);
void scnArr(int *arr, int N);
void prtArr(int *arr, int N);
void sortQuick(int arr[], int *ed);
int *randPointer(int *st, int *ed);

int main() {
    srand(time(NULL));
    int len;
    scanf("%d", &len);
    int arr[len];
    scnArr(arr, len);
    sortQuick(arr, &arr[len-1]);
    prtArr(arr, len);
    return 0;
}

void sortQuick(int *st, int *ed) {
    if (ed <= st) return;
    swap(randPointer(st, ed), ed);
    int piv = *ed;
    int *left = st, *right = st;
    while (right < ed) {
        if (*right < piv) swap(left++, right++);
        else right++;
    }
    swap(left, ed);
    sortQuick(st, left-1);
    sortQuick(left+1, ed);
}

int *randPointer(int *a, int *b) {
    return a + rand() % (b-a+1);
}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
void prtArr(int *arr, int N) {
    for (int i = 0; i < N; i++) {
        printf("%d ", arr[i]);
    }
}
void scnArr(int *arr, int N) {
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }
}
