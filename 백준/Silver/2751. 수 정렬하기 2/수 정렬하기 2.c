#include <stdio.h>

void prt_arr(int *arr, int N) {
    for (int i = 0; i < N; i++) {
        printf("%d\n", arr[i]);
    }
}
void scn_arr(int *arr, int N) {
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }
}
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
int max(int *arr, int N) {
    int max = arr[0];
    for (int i = 0; i < N; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}
int min(int *arr, int N) {
    int min = arr[0];
    for (int i = 0; i < N; i++) {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}

void sort_bubble(int *arr, int N);
void sort_selection(int *arr, int N);
void sort_insertion(int *arr, int N);
void sort_counting(int *arr, int N);

int main(int argc, char **argv) {
    int N;
    scanf("%d", &N);
    int arr[N];
    scn_arr(arr, N);
    if (N>1) sort_counting(arr, N);
    prt_arr(arr, N);
    return 0;
}

void sort_counting(int *arr, int N) {
    int mx = max(arr, N);
    int mn = min(arr, N);
    int len = mx - mn + 1;
    int arr_idx[len]; // 인덱스 담을 배열
    for (int i = 0; i < len; i++) {
        arr_idx[i] = 0;
    } // 인덱스 배열 0으로 초기화
    for (int i = 0; i < N; i++) {
        arr_idx[arr[i]-mn] = 1;
    } // 인덱스 배열의 값-최솟값 자리에 1 대입
    for (int i = 1; i < len; i++) {
        arr_idx[i] += arr_idx[i-1];
    } // 점화식 이용해 값-최솟값 자리에 인덱스+1 담음
    int arr_tmp[N]; // 임시 배열
    for (int i = 0; i < N; i++) {
        arr_tmp[arr_idx[arr[i]-mn]-1] = arr[i];
    } // 임시 배열에 정렬
    for (int i = 0; i < N; i++) {
        arr[i] = arr_tmp[i];
    } // 배열 복사
}
