#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
priority_queue < pair<int, vector<int>>> pq;
vector<vector<int>> graph(200001);
int parent[200001];
int m, n;

int find_parent(int x) {
	if (x == parent[x]) return x;
	else {
		parent[x] = find_parent(parent[x]);
		return parent[x];
	}
}

void make_union(int x, int y) {
	x = find_parent(x);
	y = find_parent(y);
	if (x != y) {
		if (x < y) 	parent[y] = parent[x];
		else parent[x] = parent[y];
	}
}


int main() {
	/*
		6497 전력난
		- 가로등 중 일부를 소등
		- 도시에 있는 모든 두집 쌍에 대해 불이 켜진 길로만 서로 왕래할 수 있도록
		- 위 조건을 지키며 절약할 수 있는 최대 액수
		-> 최소 스패닝 트리
	*/
	ios::sync_with_stdio(false);  
	cin.tie(NULL); 
	cout.tie(NULL);
	while (true) {
		cin >> m >> n;
		if (m == 0 && n == 0) break;
		int total = 0;

		graph = vector<vector<int>>(200001);
		pq = priority_queue<pair<int, vector<int>>>();
		memset(parent, 0, sizeof(parent));

		for (int i = 0; i < n; i++) {
			int x, y, z; cin >> x >> y >> z; // x - y 사이 양방향 도로, 거리 z미터
			graph[x].push_back(y);
			graph[y].push_back(x);
			total += z;
			pq.push({ -z, {x, y} }); // z가 작은 순으로 pop
		}
		for (int i = 0; i < m + 1; i++) {
			parent[i] = i;
		}

		int answer = 0;
		while (!pq.empty()) {
			int cost = pq.top().first;
			vector<int> loc = pq.top().second;
			int x = loc[0];
			int y = loc[1];
			pq.pop();
			if (find_parent(x) != find_parent(y)) {
				make_union(x, y);		
				answer -= cost;
			}
		}
		cout << total - answer << endl;
	}
}