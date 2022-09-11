#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
int n, m; 
vector<pair<int, pair<int, int>>> road;
vector<int> parent(100001);

int find_parent(int a) {
	if (parent[a] != a) parent[a] = find_parent(parent[a]);
	return parent[a];
}

void union_parent(int a, int b) {
	a = find_parent(a);
	b = find_parent(b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}


int main() {
	/*
		1647 도시 분할 계획
		- 분리된 마을 안에 집들이 서로 연결되도록 분할
		- 마을에 집이 하나 이상
		- 분리된 마을 안에서도 임의의 두집 사이에 경로가 존재하는 한 없애기 가능
		- 유지비 최소로
		-> 최소 스패닝 트리 구축 - 가장 큰 코스트의 길 
	*/
	ios::sync_with_stdio(0); cin.tie(0);
	cin >> n >> m;
	int INF = 987654321;

	for (int i = 0; i < m; i++) {
		int a, b, c; cin >> a >> b >> c;
		road.push_back({ c, {a, b} });
	}

	for (int i = 1; i < n + 1; i++) parent[i] = i;

	sort(road.begin(), road.end()); // 비용 오름 차순 정렬
	int idx = 0;
	int trail = 0;
	int total = 0;
	while (idx != m) {
		int cost = road[idx].first;
		int a = road[idx].second.first;
		int b = road[idx].second.second;
		if (find_parent(a) != find_parent(b)) {
			total += cost;
			trail += 1;
			if (trail == n - 1) {
				total -= cost;
				break;
			}
			union_parent(a, b);
		}
		idx++;
	}
	cout << total;
}