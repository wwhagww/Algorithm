#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int L(int* arr, int n, int m) {
    int mx = 0;
    for (int i=0; i<n-1; i++) {
        for (int j=0; j<m-2; j++) {
            int cand[4];
            cand[0] = arr[m*i+j] + arr[m*i+j+1] + arr[m*i+j+2] + arr[m*(i+1)+j];
            cand[1] = arr[m*i+j] + arr[m*i+j+1] + arr[m*i+j+2] + arr[m*(i+1)+j+2];
            cand[2] = arr[m*i+j] + arr[m*(i+1)+j] + arr[m*(i+1)+j+1] + arr[m*(i+1)+j+2];
            cand[3] = arr[m*i+j+2] + arr[m*(i+1)+j] + arr[m*(i+1)+j+1] + arr[m*(i+1)+j+2];
            for (int k=0; k<4; k++) {
                if (cand[k] > mx) mx = cand[k];
            }
        }
    }
    for (int i=0; i<n-2; i++) {
        for (int j=0; j<m-1; j++) {
            int cand[4];
            cand[0] = arr[m*i+j] + arr[m*i+j+1] + arr[m*(i+1)+j] + arr[m*(i+2)+j];
            cand[1] = arr[m*i+j] + arr[m*i+j+1] + arr[m*(i+1)+j+1] + arr[m*(i+2)+j+1];
            cand[2] = arr[m*i+j] + arr[m*(i+1)+j] + arr[m*(i+2)+j] + arr[m*(i+2)+j+1];
            cand[3] = arr[m*i+j+1] + arr[m*(i+1)+j+1] + arr[m*(i+2)+j] + arr[m*(i+2)+j+1];
            for (int k=0; k<4; k++) {
                if (cand[k] > mx) mx = cand[k];
            }
        }
    }
    return mx;
}
int I(int* arr, int n, int m) {
    int mx = 0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m-3; j++) {
            int cand;
            cand = arr[m*i+j] + arr[m*i+j+1] + arr[m*i+j+2] + arr[m*i+j+3];
            if (cand > mx) mx = cand;
        }
    }
    for (int i=0; i<n-3; i++) {
        for (int j=0; j<m; j++) {
            int cand;
            cand = arr[m*i+j] + arr[m*(i+1)+j] + arr[m*(i+2)+j] + arr[m*(i+3)+j];
            if (cand > mx) mx = cand;
        }
    }
    return mx;
}
int O(int* arr, int n, int m) {
    int mx = 0;
    for (int i=0; i<n-1; i++) {
        for (int j=0; j<m-1; j++) {
            int cand;
            cand = arr[m*i+j] + arr[m*i+j+1] + arr[m*(i+1)+j] + arr[m*(i+1)+j+1];
            if (cand > mx) mx = cand;
        }
    }
    return mx;
}
int Z(int* arr, int n, int m) {
    int mx = 0;
    for (int i=0; i<n-1; i++) {
        for (int j=0; j<m-2; j++) {
            int cand[2];
            cand[0] = arr[m*i+j] + arr[m*i+j+1] + arr[m*(i+1)+j+1] + arr[m*(i+1)+j+2];
            cand[1] = arr[m*i+j+1] + arr[m*i+j+2] + arr[m*(i+1)+j] + arr[m*(i+1)+j+1];
            for (int k=0; k<2; k++) {
                if (cand[k] > mx) mx = cand[k];
            }
        }
    }
    for (int i=0; i<n-2; i++) {
        for (int j=0; j<m-1; j++) {
            int cand[2];
            cand[0] = arr[m*i+j] + arr[m*(i+1)+j] + arr[m*(i+1)+j+1] + arr[m*(i+2)+j+1];
            cand[1] = arr[m*i+j+1] + arr[m*(i+1)+j] + arr[m*(i+1)+j+1] + arr[m*(i+2)+j];
            for (int k=0; k<2; k++) {
                if (cand[k] > mx) mx = cand[k];
            }
        }
    }
    return mx;
}
int T(int* arr, int n, int m) {
    int mx = 0;
    for (int i=0; i<n-1; i++) {
        for (int j=0; j<m-2; j++) {
            int cand[2];
            cand[0] = arr[m*i+j] + arr[m*i+j+1] + arr[m*i+j+2] + arr[m*(i+1)+j+1];
            cand[1] = arr[m*(i+1)+j] + arr[m*(i+1)+j+1] + arr[m*(i+1)+j+2] + arr[m*i+j+1];
            for (int k=0; k<2; k++) {
                if (cand[k] > mx) mx = cand[k];
            }
        }
    }
    for (int i=0; i<n-2; i++) {
        for (int j=0; j<m-1; j++) {
            int cand[2];
            cand[0] = arr[m*i+j] + arr[m*(i+1)+j] + arr[m*(i+1)+j+1] + arr[m*(i+2)+j];
            cand[1] = arr[m*i+j+1] + arr[m*(i+1)+j] + arr[m*(i+1)+j+1] + arr[m*(i+2)+j+1];
            for (int k=0; k<2; k++) {
                if (cand[k] > mx) mx = cand[k];
            }
        }
    }
    return mx;
}
int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    int* arr = malloc(sizeof(int) * N * M);

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            scanf("%d", &arr[i * M + j]);
        }
    }

    int mx = 0;
    int (*funcs[5])(int*, int, int) = {L, I, O, Z, T};
    
    for (int i=0; i<5; i++) {
        int cand = funcs[i](arr, N, M);
        if (cand > mx) mx = cand;
    }
    printf("%d\n", mx);
    free(arr);
    return 0;
}
