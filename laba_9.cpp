#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <time.h>
#include <queue>

void BFS(int** G, int* vis, int numG, int cur) {
  std::queue <int> q;
  vis[cur] = 1;
  q.push(cur);
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    printf(" % 3d", v);
    for (int i = 0; i < numG; i++) {
      if (vis[i] == 0 && G[v][i] == 1) {
        q.push(i);
        vis[i] = 1;
      }
    }
  }
}

void BFSD(int** G, int* dist, int numG, int cur) {
  std::queue <int> q;
  int v;
  for (int i = 0; i < numG; i++) {
    dist[i] = -1;
  }
  dist[cur] = 0;
  q.push(cur);
  while (!q.empty()) {
    v = q.front();
    q.pop();
    for (int i = 0; i < numG; i++) {
      if (G[v][i] == 1 && dist[i] == -1) {
        q.push(i);
        dist[i] = dist[v] + 1;
      }
    }
  }
  printf("Расстояние от %d вершины до:\n", cur);
  for (int i = 0; i < numG; i++) {
    printf("%d: %d\n", i, dist[i]);
  }
}

int main() {
  setlocale(LC_ALL, "Russian");
  int** G;
  int* visited;
  int* dist;
  int numG, cur;
  srand(time(NULL));
  printf("Введите кол-во вершин ");
  scanf_s("%d", &numG);

  G = (int**)malloc(numG * sizeof(int*));
  for (int i = 0; i < numG; i++) {
    G[i] = (int*)malloc(numG * sizeof(int));
  }
  visited = (int*)malloc(numG * sizeof(int));
  dist = (int*)malloc(numG * sizeof(int));
  for (int i = 0; i < numG; i++) {
    visited[i] = 0;
    dist[i] = -1;
    for (int j = i; j < numG; j++) {
      G[i][j] = G[j][i] = (i == j ? 0 : rand() % 2);
    }
  }
  for (int i = 0; i < numG; i++) {
    for (int j = 0; j < numG; j++) {
      printf("%3d", G[i][j]);
    }
    printf("\n");
  }
  printf("Введите начальную вершину: ");
  scanf_s("%d", &cur);
  printf("Порядок обхода ");
  BFS(G, visited, numG, cur);
  printf("\n");
  BFSD(G, dist, numG, cur);
}