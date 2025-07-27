#include <stdio.h>
#include <string.h>

int visited[10000];
char path[10000][10001];
int queue[10000];
int front, rear;

int D(int n) { return (2 * n) % 10000; }
int S(int n) { return (n == 0) ? 9999 : n - 1; }
int L(int n) { return (n % 1000) * 10 + (n / 1000); }
int R(int n) { return (n % 10) * 1000 + (n / 10); }

void solve(int A, int B) {
  memset(visited, 0, sizeof(visited));
  front = rear = 0;

  visited[A] = 1;
  queue[rear++] = A;
  strcpy(path[A], "");

  while (front < rear) {
    int cur = queue[front++];

    if (cur == B) {
      printf("%s\n", path[cur]);
      return;
    }

    int next;
    char ops[] = {'D', 'S', 'L', 'R'};
    int (*funcs[])(int) = {D, S, L, R};

    for (int i = 0; i < 4; i++) {
      next = funcs[i](cur);
      if (!visited[next]) {
        visited[next] = 1;
        queue[rear++] = next;
        strcpy(path[next], path[cur]);
        int len = strlen(path[next]);
        path[next][len] = ops[i];
        path[next][len+1] = '\0';
      }
    }
  }
}
int main() {
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    int A, B;
    scanf("%d %d", &A, &B);
    solve(A, B);
  }
  return 0;
}
