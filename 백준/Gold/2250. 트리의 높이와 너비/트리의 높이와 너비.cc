#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
int n;
int r;
int max_level;

int root[10001];
int level[10001];

vector<pair<int, int>> graph(10001);
vector<int> seq;

void dfs(int now, int l) {
	level[now] = l;
	max_level = max(max_level, l);
	int left = graph[now].first;
	int right = graph[now].second;
	if (left != -1) {
		seq.insert(find(seq.begin(), seq.end(), now), left);
		dfs(left, l + 1);
	}
	if (right != -1) {
		seq.insert(find(seq.begin(), seq.end(), now) + 1, right);
		dfs(right, l + 1);
	}
}
int main() {
	/*
		2250 트리의 높이와 너비
		- 1. 이진 트리에서 같은 레벨에 있는 노드는 같은 행에 위치 
		- 2. 한 열에는 한 노드만 존재
		- 3. 임의의 노드에 왼쪽 자식은 왼쪽열 / 오른 자식은 오른열
		- 4. 비어있는 열은 없음
		너비 : 레벨의 가장 오른쪽 - 왼쪽 + 1
	*/
	cin >> n;
	memset(root, 0, sizeof(root));
	memset(level, 0, sizeof(level));

	for (int i = 0; i < n; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		graph[a] = { b, c };
		if (b != -1) root[b] = -1;
		if (c != -1) root[c] = -1;
	}
	for (int i = 1; i <= n; i++) {
		if (root[i] == 0) {
			r = i;
			break;
		}
	}

	max_level = 1;
	level[r] = 1;
	seq = { r };
	dfs(r, 1);

	int max_nubys = 0;
	int max_levels;
	for (int i = 1; i <= max_level; i++) {
		vector<int> nubys;
		for (int j = 1; j <= n; j++) {
			if (level[j] == i) { 
				nubys.push_back(find(seq.begin(), seq.end(), j) - seq.begin());
			}
		}
		int max_nuby = *max_element(nubys.begin(), nubys.end());
		int min_nuby = *min_element(nubys.begin(), nubys.end());
		int val = max_nuby - min_nuby + 1;
		if (val > max_nubys) {
			max_nubys = val;
			max_levels = i;
		}
	}
	cout << max_levels << " " << max_nubys << endl;
}